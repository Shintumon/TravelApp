from django.http import HttpResponse
from django.shortcuts import render
from .models import WhyChooseUs, MeetTheTeam


# For creating multiple views:
# def demo(request):
#     return HttpResponse("hello world")
#
# def demo(request):
#     return render(request, "home.html")
#
#
# def about(request):
#     return render(request, "about.html")
#
#
# def contact(request):
#     return render(request, "contact.html")

# For passing values:
# def demo(request):
#     name="World"
#     return render(request, "home.html", {'obj':name})
#
#
# def addition(request):
#     x = int(request.GET['num1'])
#     y = int(request.GET['num2'])
#     res = x+y
#     return render(request, "result.html",{'result':res})

# For converting static website
# def demo(request):
#     return render(request, "index.html")


# For converting static website into dynamic
def demo(request):
    obj = WhyChooseUs.objects.all()
    team = MeetTheTeam.objects.all()
    return render(request, "index.html", {'result': obj, 'teams': team})
