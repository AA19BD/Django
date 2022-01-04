from django.shortcuts import render,redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView,UpdateView,DeleteView


def news_home(request):
    news=Articles.objects.order_by("-date")[:] #objects.all
    return render(request,'news/news_home.html',{'news':news})

class NewsDetailView(DetailView):#django.views.generic(much easier)
    model = Articles
    template_name = 'news/details_view.html' #шаблон для обработки стрaницы
    context_object_name = 'article'

class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'  # шаблон для обработки стрaницы
    form_class=ArticlesForm

class NewsDeleteView(DeleteView):
    model = Articles
    success_url='/news'
    template_name = 'news/news-delete.html'  # шаблон для обработки стрaницы

def create(request):
    error=''
    if request.method=='POST':
        form=ArticlesForm(request.POST)#Получаем все данные которые ввели
        if form.is_valid():#корректно ли заполнены данные
            form.save()#save in DB
            return redirect('news_home')
        else:
            error='Form is not valid'

    form=ArticlesForm()
    data={
        'form':form,
        'error':error
    }
    return render(request,'news/create.html',data)