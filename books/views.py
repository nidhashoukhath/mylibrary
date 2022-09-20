from django.shortcuts import render, redirect
from .models import Book
from .forms import CreateBookForm

# Create your views here.
def index(request):
    books = Book.objects.all()    
    return render(request, 'books/index.html', {'books': books})

def details(request, id):
    book = Book.objects.get(id = id)
    return render(request, 'books/details.html', {'book':book})    

def create(request):
    if request.POST:
        form = CreateBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/books/')
    form = CreateBookForm()
    return render(request, 'books/create.html', {'form':form})        

def update(request, id):
    book = Book.objects.get(id = id)
    form = CreateBookForm(instance = book)
    if request.POST:
        form = CreateBookForm(request.POST,instance = book )
        if form.is_valid():
            form.save()
            return redirect(f'/books/{id}/')
    return render(request, 'books/update.html', {'form':form})    


def delete(request, id):
    book = Book.objects.get(id = id)
    book.delete()
    return redirect('/books/')

