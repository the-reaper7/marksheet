from django.db import models

# Create your models here.


class Student(models.Model):
    classes = [(f'{x}', x) for x in range(1, 13)]
    section = [(f'{chr(x)}', chr(x)) for x in range(65, 73)]
    
    serial_number = models.PositiveIntegerField(primary_key=True)
    student_photo = models.ImageField(upload_to="images")
    student_name = models.CharField(max_length=50)
    student_surname = models.CharField(max_length=50)
    student_class = models.CharField(max_length=2, choices=classes)
    student_section = models.CharField(max_length=1, choices=section)
    student_roll_no = models.PositiveIntegerField()
    
    marks_maths_semester_1 = models.PositiveIntegerField(default=0, null=True)
    marks_science_semester_1 = models.PositiveIntegerField(default=0, null=True)
    marks_english_semester_1 = models.PositiveIntegerField(default=0, null=True)
    marks_hindi_semester_1 = models.PositiveIntegerField(default=0, null=True)
    marks_computer_science_semester_1 = models.PositiveIntegerField(default=0, null=True)
    
    marks_maths_semester_2 = models.PositiveIntegerField(default=0, null=True)
    marks_science_semester_2 = models.PositiveIntegerField(default=0, null=True)
    marks_english_semester_2 = models.PositiveIntegerField(default=0, null=True)
    marks_hindi_semester_2 = models.PositiveIntegerField(default=0, null=True)
    marks_computer_science_semester_2 = models.PositiveIntegerField(default=0, null=True)
    
    marks_maths_semester_3 = models.PositiveIntegerField(default=0, null=True)
    marks_science_semester_3 = models.PositiveIntegerField(default=0, null=True)
    marks_english_semester_3 = models.PositiveIntegerField(default=0, null=True)
    marks_hindi_semester_3 = models.PositiveIntegerField(default=0, null=True)
    marks_computer_science_semester_3 = models.PositiveIntegerField(default=0, null=True)
    
    marks_maths_semester_4 = models.PositiveIntegerField(default=0, null=True)
    marks_science_semester_4 = models.PositiveIntegerField(default=0, null=True)
    marks_english_semester_4 = models.PositiveIntegerField(default=0, null=True)
    marks_hindi_semester_4 = models.PositiveIntegerField(default=0, null=True)
    marks_computer_science_semester_4 = models.PositiveIntegerField(default=0, null=True)

    def __str__(self):
        return self.student_name

    class Meta:
        verbose_name_plural = "Students Marksheet"
