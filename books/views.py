from django.shortcuts import render, redirect
from .models import Book
from .forms import CreateBookForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

@login_required
def index(request):
    books = Book.objects.all()    
    return render(request, 'books/index.html', {'books': books})

@login_required
def details(request, id):
    book = Book.objects.get(id = id)
    return render(request, 'books/details.html', {'book':book})    

@login_required
def create(request):
    if request.POST:
        form = CreateBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/books/')
    form = CreateBookForm()
    return render(request, 'books/create.html', {'form':form})        

@login_required
def update(request, id):
    book = Book.objects.get(id = id)
    form = CreateBookForm(instance = book)
    if request.POST:
        form = CreateBookForm(request.POST,instance = book )
        if form.is_valid():
            form.save()
            return redirect(f'/books/{id}/')
    return render(request, 'books/update.html', {'form':form})    

@login_required
def delete(request, id):
    book = Book.objects.get(id = id)
    book.delete()
    return redirect('/books/')

def sign_up(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    form = UserCreationForm()
    return render(request, 'registration/sign_up.html', {'form':form})      