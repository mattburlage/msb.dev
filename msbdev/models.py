from django.db import models


# Create your models here.
class TextCopy(models.Model):
    name = models.CharField(max_length=64, verbose_name='Internal Name')
    html = models.TextField(verbose_name='HTML')
    classes = models.CharField(max_length=255, null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class ContactForm(models.Model):
    email = models.EmailField()
    note = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class AppSetting(models.Model):
    name = models.CharField(max_length=128)
    content = models.TextField(null=True)

    def __str__(self):
        return self.name
