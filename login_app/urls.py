from django.urls import path
from login_app import views

#TEMPLATE TAGGING
app_name = 'login_app'

#url list
urlpatterns = [
    path('user_login/',views.user_login,name='user_login'),
    path('register/',views.register,name='register'),
    path('home/',views.home,name='home'),
]
