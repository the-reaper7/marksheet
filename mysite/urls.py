from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add/', views.add, name='add'),
    path('search/', views.search, name='search'),
    path('signup/', views.signup, name='signup'),
    path('search/studentprofile/<int:pk>', views.student_profile, name='student_profile'),
    path('search/studentprofile/edit/<int:pk>', views.edit_profile, name='edit_student_profile'),
    path('search/studentprofile/delete/<int:pk>', views.delete_profile, name='delete_student_profile'),
    path('search/studentprofile/get-marks/<int:pk>', views.get_marks, name='get_marks'),
]
