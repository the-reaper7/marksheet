from .forms import StudentForm
from .models import Student
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse
# Create your views here.


def index(request):
    return render(request, 'home.html')


def search(request):
    context = {}
    if "searchStudent" in request.GET:
        qs = Student.objects.filter(
            student_name__icontains=request.GET.get('searchStudent'))
        context['filter'] = qs
    return render(request, 'search.html', context=context)


def student_profile(request, pk):
    student = Student.objects.all().filter(serial_number=pk)
    name = student.values()[0]['student_name']
    context = {'student': student, 'name': name}
    return render(request, 'student_profile.html', context=context)


@login_required
def add(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'add.html', context=context)


@login_required
def edit_profile(request, pk):
    student = Student.objects.get(serial_number=pk)
    form = StudentForm(instance=student)
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
        return redirect('search')
    context = {'form': form, 'name': student}
    return render(request, 'add.html', context=context)


@login_required
def delete_profile(request, pk):
    student = Student.objects.get(serial_number=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('home')
    context = {'name': student}
    return render(request, 'delete_student_profile.html', context=context)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'registration/signup.html', context=context)


def get_marks(request, pk):
    student = Student.objects.all().filter(serial_number=pk).values()[0]
    if request.method == 'GET':
        data = [{
            "semester 1": [
                student['marks_maths_semester_1'],
                student['marks_science_semester_1'],
                student['marks_computer_science_semester_1'],
                student['marks_hindi_semester_1'],
                student['marks_english_semester_1'],
            ],
            "semester 2": [
                student['marks_maths_semester_2'],
                student['marks_science_semester_2'],
                student['marks_computer_science_semester_2'],
                student['marks_hindi_semester_2'],
                student['marks_english_semester_2'],
            ],
            "semester 3": [
                student['marks_maths_semester_3'],
                student['marks_science_semester_3'],
                student['marks_computer_science_semester_3'],
                student['marks_hindi_semester_3'],
                student['marks_english_semester_3'],
            ],
            "semester 4": [
                student['marks_maths_semester_4'],
                student['marks_science_semester_4'],
                student['marks_computer_science_semester_4'],
                student['marks_hindi_semester_4'],
                student['marks_english_semester_4'],
            ],
            "average": {
                "semester 1": (student['marks_maths_semester_1'] + student['marks_science_semester_1'] + student['marks_computer_science_semester_1'] + student['marks_hindi_semester_1'] + student['marks_english_semester_1'])/5,
                "semester 2": (student['marks_maths_semester_2'] + student['marks_science_semester_2'] + student['marks_computer_science_semester_2'] + student['marks_hindi_semester_2'] + student['marks_english_semester_2'])/5,
                "semester 3": (student['marks_maths_semester_3'] + student['marks_science_semester_3'] + student['marks_computer_science_semester_3'] + student['marks_hindi_semester_3'] + student['marks_english_semester_3'])/5,
                "semester 4": (student['marks_maths_semester_4'] + student['marks_science_semester_4'] + student['marks_computer_science_semester_4'] + student['marks_hindi_semester_4'] + student['marks_english_semester_4'])/5
            }
        }]
        return JsonResponse(data, safe=False)
    return JsonResponse([], safe=False)
