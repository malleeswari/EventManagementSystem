from django.contrib import admin
from django.urls import path,include 
from home import views


urlpatterns = [

    path("register",views.registerPage,name='regsiter'),

    path("login",views.loginPage,name='login'),
    
    path("logout",views.logoutUser,name='logout'), 
    
    path("",views.index,name='home'),
    
    path("about",views.about,name='about'),

    path("eventmanagement",views.event,name='eventmanagement'),
    
    path("technicalevent",views.technicalevent,name='technicalevent'),

    path("partiesevent",views.partiesevent,name='partiesevent'),

    path("collegeevent",views.collegeevent,name='collegeevent'),

    path("eventadvisor",views.eventadvisor,name='eventadvisor'),

    path("weddingevent",views.weddingevent,name='weddingevent'),
    
    path("confirm",views.confirm,name='confirm'),

    path("payment",views.payment,name='payment'),

    path("contact",views.contact,name='contact'),

    path("weddingevent", views.wedding_event_view, name="wedding_event"),

    path("partyevent", views.party_event_view, name="party_event"),

    path("technicalevent", views.technical_event_view, name="technical_event"),

    path("collegeevent", views.college_event_view, name="college_event"),
   
    
]
