from django.contrib import messages
from django.http import Http404
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from msbdev.forms import ContactFormForm
from msbdev.models import TextCopy


def index(request, formsent=False):
    if request.method == "POST":
        return formsubmit(request)

    mydivs = TextCopy.objects.filter(active=True)
    divlist = {}

    for item in mydivs:
        divlist[item.name] = item.html

    form = ContactFormForm()

    context = {
        'textcopy': divlist,
        'form': form,
        'formsent': formsent,
    }

    return render(request, 'msbdev/msbdev.html', context=context)


def formsubmit(request):
    if request.method == 'POST':
        forminc = ContactFormForm(request.POST)

        if forminc.is_valid():
            form = forminc.save(commit=False)
            form.save()

            return index(request, True)
        else:
            raise Http404(forminc.errors)
