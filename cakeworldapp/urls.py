
from django.urls import path, include

from cakeworldapp import views

urlpatterns = [

    path('',views.demo,name="demo"),



    # path('',views.about,name="about"),
    # path('',views.contact,name="contact"),
    # path('',views.menu,name="menu"),
    # path('',views.service,name="service"),
    # path('',views.team,name="team"),
    # path('',views.testimonial,name="testimonail"),


]
