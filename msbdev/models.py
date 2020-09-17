from django.db import models


class TextCopy(models.Model):
    name = models.CharField(max_length=64, verbose_name='Internal Name')
    html = models.TextField(verbose_name='HTML')
    classes = models.CharField(max_length=255, null=True, blank=True)
    active = models.BooleanField(default=True)

    @staticmethod
    def get_html(name):
        try:
            text_copy = TextCopy.objects.get(name=name)

            return text_copy.html
        except TextCopy.DoesNotExist:
            return None


    def __str__(self):
        return self.name


class ContactForm(models.Model):
    email = models.EmailField()
    note = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)
    copies = models.IntegerField(default=1)

    def __str__(self):
        return self.email


class AppSetting(models.Model):
    name = models.CharField(max_length=128)
    content = models.TextField(null=True)

    @staticmethod
    def get_setting(setting_name, default=None):
        try:
            return AppSetting.objects.get(name=setting_name).content
        except AppSetting.DoesNotExist:
            return default

    def __str__(self):
        return self.name


class WorkItem(models.Model):
    name = models.CharField(max_length=128)
    active = models.BooleanField(default=False)
    order = models.IntegerField()
    label = models.CharField(max_length=64, null=True, blank=True)
    tech_used = models.CharField(max_length=64, null=True, blank=True)
    short_text = models.TextField(null=True, blank=True)
    long_text = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)

    def name_safe(self):
        return self.label if self.label else self.name

    def image_url_safe(self):
        if self.image:
            return self.image.url
        elif self.image_url:
            return self.image_url
        else:
            return None

    def __str__(self):
        return self.name
