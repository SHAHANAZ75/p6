from django.urls import path
from mypp import views
app_name="mypp"

urlpatterns = [
    path('trial/',views.trial,name="trial"),
    path('profile/',views.profile,name="profile"),
]
