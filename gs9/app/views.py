from django.shortcuts import render

# Create your views here.
def index(request, group_name):
    print("Group name... ", group_name)
    context = {"groupname": group_name}
    return render(request, 'app/index.html', context)