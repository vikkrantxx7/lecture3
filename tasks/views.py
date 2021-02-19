from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

class NewTaskForm(forms.Form):
    task = forms.CharField(label='New Task')

# Create your views here.
def tasks(request):
    if 'tasksList' not in request.session:
        request.session['tasksList'] = []
    return render(request, 'tasks/index.html', {
        'tasks': request.session['tasksList']
    })

def add(request):
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data['task']
            request.session['tasksList'] += [task]
            return HttpResponseRedirect(reverse("tasks"))
        else:
            return render(request, 'tasks/add.html', {
                "form": form
            })
    return render(request, 'tasks/add.html', {
        "form": NewTaskForm()
    })