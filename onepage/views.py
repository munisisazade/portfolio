from django.shortcuts import render
from .models import WebsiteCommon, HeaderSection, Menu, AboutSection, Project, Offers, FooterIcon, CallSection


def index(request):
    context = {}
    context["common"] = WebsiteCommon.objects.last()
    context["header"] = HeaderSection.objects.last()
    context["menu_list"] = Menu.objects.all()
    context["about"] = AboutSection.objects.last()
    context["offer_list"] = Offers.objects.all()
    context["project_list"] = Project.objects.all()
    context["footer_list"] = FooterIcon.objects.all()
    context["call"] = CallSection.objects.last()
    return render(request, "index.html", context)

# Create your views here.
