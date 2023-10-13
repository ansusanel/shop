from django.urls import path
from.import views

urlpatterns = [
    path('',views.userindex,name='userindex'),
    path('register',views.register,name='register'),
    path('cardview',views.cardview,name='cardview'),
    path('order/<int:productid>',views.order,name='order'),
    path('login',views.login,name='login'), 
    path('contact',views.contact,name='contact'),
    path('onecardview/<int:productid>',views.onecardview,name='onecardview'),
    path('orderdata',views.orderdata,name='orderdata'),
    path('feedbackform',views.feedbackform,name='feedbackform'),
    path('feedbackdata',views.feedbackdata,name='feedbackdata'),
    path('Registrationdata',views.Registrationdata,name='Registrationdata'),
    path('publicdata',views.publicdata,name='publicdata'),
    path('userlogout',views.userlogout,name='userlogout'),    
]