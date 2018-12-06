from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from .forms import *
# Create your views here.


class HomeView(TemplateView):
    template_name = 'notifier/home.html'


def someform(request):

    if request.method == 'POST':
        form = SampleForm(request.POST)
        if form.is_valid():
            form.save()
            print("form saved")
            messages.success(request,
                             f'Form created successfully!\n')
            return redirect('home')
    else:
        form = SampleForm()

        context = {'form': form}
        return render(request,
                      'notifier/sample_form.html',
                      context)
