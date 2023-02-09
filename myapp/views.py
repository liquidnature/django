from django.shortcuts import render
from .models import Room


# rooms = [
#     {'id':1, 'name': 'Lets learn Python!!'},
#     {'id':2, 'name': 'Django is second'},
#     {'id':3, 'name': 'Anything next'},
# ]

def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, "myapp/home.html", context)


def room(request, pk):

    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'myapp/room.html', context)


