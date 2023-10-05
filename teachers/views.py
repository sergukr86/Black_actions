from django.shortcuts import render
from django.http import HttpResponse

from teachers.models import Teacher


def show_teachers(request):
    all_teachers = list(Teacher.objects.all())
    return HttpResponse(all_teachers)


