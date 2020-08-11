from django.urls import path
from mypp import views
app_name="mypp"

urlpatterns = [
    path('trial/',views.trial,name="trial"),
    path('profile/',views.profile,name="profile"),
    path('get_demo/',views.get_demo,name="get_demo"),
    path('post_demo/',views.post_demo,name="post_demo"),
    path('register/',views.register,name="register"),
]
