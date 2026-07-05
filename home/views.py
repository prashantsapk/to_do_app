# To-Do App
# tasks add/edit/delete, mark complete.
# focus: models, forms, admin



from django.shortcuts import render,redirect,get_object_or_404
from .models import tasks
from .forms import Form

# Create your views here.

def homepage_view(request):
    
    tasksobj = tasks.objects.all()
    

    return render(request,'homepage.html',{'tasksobj' : tasksobj})

def addtask_view(request):

    if request.method == 'POST':
        sumbitedform = Form(request.POST)
        if sumbitedform.is_valid():
            sumbitedform.save()
            return redirect('homepage')
    else:
        sumbitedform = Form()
        
   

    return  render(request,'add_task.html',{'Form':sumbitedform})

def deletetask_view(request):
    if request.method =="POST":
        id = request.POST.get('id')
        deleteobj = get_object_or_404(tasks,id=id)
        deleteobj.delete()


        
    

    return redirect('homepage')

    
