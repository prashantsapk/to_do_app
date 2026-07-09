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


def edittask_view(request):

    id = request.GET.get('id2')

    if request.method == "GET":
        obj = get_object_or_404(tasks,id = id)
        filledformobj = Form(instance = obj)
    else:
        obj = get_object_or_404(tasks,id = id)
        newfilledform = Form(request.POST,instance = obj)
        if newfilledform.is_valid():
            newfilledform.save()
        
        return redirect('homepage')


    return render(request,'edit_task.html',{'Form':filledformobj})



def markcompleted_view(request):
    id = request.POST.get('id1')
    
    if request.method =="POST":
        obj = get_object_or_404(tasks,id = id)
        obj.status = 'completed'
        obj.save()
       
    return redirect('homepage')
