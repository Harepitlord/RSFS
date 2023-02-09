from django.urls import path
from . import views



app_name='UserManagement'
urlpatterns=[
    path('login',views.Login.as_view(),name='Login'),
    path('logout',views.Logout.as_view(),name='Logout'),
    path('signup',views.Signup.as_view(),name='Signup'),
]