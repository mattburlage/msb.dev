from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from msbdev.models import AppSetting, ContactForm
from msbdev.serializers import ContactFormSerializer


def index(request):
    """ Handle standard page view"""
    # Render template
    context = {
        'show_numbers': AppSetting.get_setting('show_numbers'),
        'show_cur_numbers': AppSetting.get_setting('show_cur_numbers'),
    }
    return render(request, 'msbdev/msbdev2.html', context)


def index2(request):
    """ Handle standard page view"""
    # Render template
    return render(request, 'msbdev/msbdev3.html')


@api_view(['POST'])
def submit_form(request):
    serializer = ContactFormSerializer(data=request.data)

    if serializer.is_valid():
        email = serializer.validated_data['email']
        note = serializer.validated_data['note']

        if email in AppSetting.objects.get(name="EMAIL_BLACKLIST").content:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        existing_form = ContactForm.objects.filter(email=email, note=note)
        if existing_form:
            existing_form = existing_form[0]
            existing_form.copies += 1
            existing_form.save()

            return Response(data=serializer.data, status=status.HTTP_200_OK)

        serializer.save()

        return Response(data=serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
