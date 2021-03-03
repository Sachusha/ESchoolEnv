from django.shortcuts import render, redirect, get_object_or_404
from .models import SchoolProfile
from django.urls import reverse_lazy
from django.views import generic
from . import forms
# Create your views here.


# SchoolRegistration button

def index(request):
    return render(request, 'static_settings/index.html')


# Registering the school profile name


def schoolprofile(request):
    model_object = SchoolProfile.objects.all()
    if request.method == 'POST':
        form = forms.SchoolProfileForms(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('static_settings:SchoolProfileForms')
    else:
        form = forms.SchoolProfileForms()
    return render(request, 'static_settings/SchoolProfile.html', {'form': form, 'data': model_object})

# delete


def school_delete(request, pk):
    post = get_object_or_404(SchoolProfile, pk=pk)
    post.delete()
    return redirect('static_settings:SchoolProfileForms')


# edit

def school_edit(request, pk):
    template = "static_settings/SchoolProfile.html"
    post = get_object_or_404(SchoolProfile, pk=pk)
    model_object = SchoolProfile.objects.all()
    if request.method == 'POST':
        form = forms.SchoolProfileForms(request.POST, instance=post)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('static_settings:SchoolProfileForms')
    else:
        form = forms.SchoolProfileForms(instance=post)
        context = {
            'form': form,
            'post': post,
            'data': model_object,
        }
    return render(request, template, context)

# viewing


class SchoolProfileView(generic.DetailView):
    model = SchoolProfile
    template_name = 'static_settings/SchoolProfileview.html'

#
# class SchoolProfileupdate(generic.UpdateView):
#     model = SchoolProfile
#     fields = ['profile_name', 'profile_address', 'profile_contactno', 'profile_email']
#     template_name = 'static_settings/SchoolProfileupdate.html'

