from django.shortcuts import render
from .models import Group, Chat

# Create your views here.
def index(request, group_name):
    print("Group name... ", group_name)

    group = Group.objects.filter(name=group_name).first()
    chats = []
    if group:
        chats = Chat.objects.filter(group=group)
        print(group)
    else:
        group = Group(name=group_name)
        group.save()

    context = {"groupname": group_name, "chats": chats}
    return render(request, 'app/index.html', context)