##
# APP: agenda - views.py
##
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'agenda/index.html')