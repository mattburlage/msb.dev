from rest_framework import serializers

from msbdev.models import ContactForm


class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactForm
        fields = ['email', 'note']
