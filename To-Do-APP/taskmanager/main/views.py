from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskForm

# Create your views here.




def index(request):
    tasks=Task.objects.order_by('title')[:]
    return render(request,'main/index.html',{"title":"Home","tasks":tasks})


#
def create(request):
    error=""
    if request.method=="POST":
        form=TaskForm(request.POST)#There is new data to post
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error="NOT VALID FORM"


    form=TaskForm()
    context={
        'form':form,
        'error':error
    }

    return render(request,'main/create.html',context)



