from django.db import models

# Create your models here.
class WebsiteCommon(models.Model):
    brand = models.CharField(max_length=255)
    copyright_text = models.CharField(max_length=255)
    offer_background = models.ImageField(upload_to="offer/", null=True, blank=True)

    def __str__(self):
        return "{}".format(self.brand)

class HeaderSection(models.Model):
    background_image = models.ImageField(upload_to="header/")
    main_title = models.CharField(max_length=255)
    sub_title = models.TextField()
    button_text = models.CharField(max_length=255,null=True, blank=True)

    def __str__(self):
        return"{}".format(self.main_title)

class Menu(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    order = models.IntegerField(default=0)

    def __str__(self):
        return"{}".format(self.name)

    class Meta:
        ordering = ("order",)

class AboutSection(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    background_picture = models.ImageField(upload_to="about/")
    button_text = models.CharField(max_length=255,null=True, blank=True)

    def __str__(self):
        return "{}".format(self.title)

class Project(models.Model):
    main_title = models.CharField(max_length=255)
    picture = models.ImageField(upload_to="project/")
    title = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.main_title)

class Offers(models.Model):
    main_title = models.CharField(max_length=255)
    icon = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255)
    text = models.TextField()


class FooterIcon(models.Model):
    icon = models.CharField("icon", max_length=255, null=True, blank=True)
    link = models.TextField()

    def __str__(self):
        return "{}".format(self.icon)

class CallSection(models.Model):
    main_title = models.CharField(max_length=255, null=True, blank=True)
    button_text = models.CharField(max_length=255,null=True, blank=True)
    background_image = models.ImageField(upload_to="call/" ,null=True, blank=True)
