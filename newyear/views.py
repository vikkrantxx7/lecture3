import datetime
from django.shortcuts import render

# Create your views here.
def newYear(request):
    now = datetime.datetime.now()
    return render(request, 'newYear/index.html', {
        'newyear': now.month == 1 and now.day == 1
    })