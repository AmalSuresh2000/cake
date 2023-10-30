from django.shortcuts import render
from .models import Cake


# Create your views here.
def demo(request):
    obj=Cake.objects.all()

    return render(request,"index.html",{'result': obj})

# def about(request):
#     return render(request,"about.html")
#
# def contact(request):
#     return render(request,"contact.html")
#
# def menu(request):
#     return render(request,"menu.html")
#
# def service(request):
#     return render(request,"service.html")
#
# def team(request):
#     return render(request,"team.html")
#
# def testimonial(request):
#     return render(request,"testimonial.html")


