from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import details, skills, education, experience

def prf(request):
    detail = details.objects.all()
    skill = skills.objects.all()
    educations = education.objects.all()
    experiences = experience.objects.all()

    context = {'detail': detail, 'skills': skill, 'education': educations, 'experience': experiences}
    
    return render(request, 'index.html',context)


