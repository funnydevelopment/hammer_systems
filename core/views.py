from django.shortcuts import render


def index(request):
    return render(request, template_name="core/main_menu.html")
