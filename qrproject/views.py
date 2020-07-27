from django.shortcuts import render
from qrapp.models import Qr

def home_view(request):
    name = "Welcome to"

    obj = Qr.objects.get(id=1)
    context = {
        'name':name,
        'obj':obj,
    }

    return render(request, 'home.html', context)
   