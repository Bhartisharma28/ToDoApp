from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
def Home(request):
    MyNoteBookApp=MyNoteBookModel.objects.all()
    form= MyNoteBookModelForm()

    if request.method=='POST':
        form=MyNoteBookModelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context={'MyNoteBookApp':MyNoteBookApp, 'form':form}
    return render(request,'MyNoteBookApp/Home.html', context)

def update(request,pk):
    MyNoteBookApp=MyNoteBookModel.objects.get(id=pk)
    form= MyNoteBookModelForm(instance= MyNoteBookApp)
    if request.method== 'POST':
            form= MyNoteBookModelForm(request.POST,instance= MyNoteBookApp)
            if form.is_valid():
                form.save()
            return redirect('/')

    context={'form':form,'data':MyNoteBookApp}

    return render(request, 'MyNoteBookApp/update.html', context)

def delete(request,pk):
    item = MyNoteBookModel.objects.get(id=pk)
    if request.method== 'POST':
        item.delete()
        return redirect('Home')

    context={'item':item}
    return render(request, 'MyNoteBookApp/delete.html', context)
