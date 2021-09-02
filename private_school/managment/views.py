from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from .forms import CourseForm, TrainerForm
from .models import Course, Trainers



def base_page(request):
    return render(request, 'managment/base.html', {})



def trainers_page(request):

    trainer_list = Trainers.objects.all().order_by('last_name')

    return render(request, 'managment/trainers.html', { 'trainers' : trainer_list})


def success(request, message):
    return render(request, 'managment/success.html', {'message': message})



def trainer_add(request):
    if request.method == 'POST':
        form = TrainerForm(request.POST)
        if form.is_valid():

            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')

            form.save()

            message = first_name + " " + last_name + ' added successfully'
            
            return HttpResponseRedirect('/managment/success/' + message + '/')

    else:

        form = TrainerForm()

    return render(request, 'managment/trainer_add.html', { 'form': form })



def trainer_edit(request, id):
    trainer = Trainers.objects.get(id = id)

    if request.method == 'POST':

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        subject = request.POST.get('subject')

        trainer.first_name = first_name
        trainer.last_name = last_name
        trainer.subject = subject

        trainer.save()
        courses = request.POST.getlist('courses')
        trainer.courses.clear()
        for course in courses:
            trainer.courses.add(course)

        message = 'You have successfully edited the trainer'


        return HttpResponseRedirect('/managment/success/' + message + '/')

    else:

        courses = Course.objects.all().order_by('course_title')
        tr_courses = trainer.courses.all().order_by('course_title')
         
        context ={
            'trainer' : trainer,
            'courses' : courses,
            'tr_courses' : tr_courses,
        }

    return render(request, 'managment/trainer_edit.html', context)


def trainer_details(request, id):

    trainer = Trainers.objects.get(id = id)

    return render(request, 'managment/trainer_details.html', {'trainer' : trainer})


def trainer_delete(request, id):

    trainer = Trainers.objects.get(id = id)

    trainer.delete()

    message = 'You have successfully delete the trainer :' + trainer.first_name + " " + trainer.last_name

    return HttpResponseRedirect('/managment/success/' + message + '/')

