from django.shortcuts import render, HttpResponse , HttpResponseRedirect
from .models import *
from .forms import *

# Create your views here.
def index(request):

    d = Book.objects.all()
    # for i in d:


        # print(i.title)
        # print(i.no_pages)
        # print(i.created_by)
        # print("------------------------")

    # return HttpResponse("done")
    return render(request, 'home.html', {'info': d})


def authorform(request):
    if request.method == 'POST':
        if request.method == 'POST':
            form = author_form(request.POST , request.FILES)

            if form.is_valid():
                form.save()

            return HttpResponseRedirect('/')

    else:
        form = author_form()

    return render(request , 'author.html' , {'form' :form})


def bookform(request):
    if request.method == 'POST':
        if request.method == 'POST':
            form = book_form(request.POST)

            if form.is_valid():
                form.save()

            return HttpResponseRedirect('/')

    else:
        form = book_form()
    return render(request, 'author.html', {'form': form})