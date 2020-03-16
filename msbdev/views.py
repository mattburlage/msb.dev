from django.contrib import messages
from django.http import Http404
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from msbdev.forms import ContactFormForm
from msbdev.models import TextCopy, AppSetting
from msbdev.serializers import ContactFormSerializer


def index(request):
    """ Handle standard page view"""

    # Get the text copy items for display in the template
    mydivs = TextCopy.objects.filter(active=True)
    divlist = {}
    for item in mydivs:
        divlist[item.name] = item.html

    # Set up blank contact form
    form = ContactFormForm()

    # establish context for template
    context = {
        'textcopy': divlist,
        'form': form,
    }

    # Render template
    return render(request, 'msbdev/msbdev.html', context=context)


@api_view(['POST'])
def submit_form(request):
    serializer = ContactFormSerializer(data=request.data)

    if serializer.is_valid():
        if serializer.validated_data['email'] in AppSetting.objects.get(name="EMAIL_BLACKLIST").content:
            return Response(data=serializer.errors, status=status.HTTP_401_UNAUTHORIZED)

        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)