from django.urls import path 

from .import views

app_name = 'users'
urlpatterns = [
    path('register/',views.RegisterView.as_view(), name='register'),

    # path('login/',
    #      auth_views.LoginView.as_view(),
    #      name='login'),
    # path('logout/',
    #      auth_views.LogoutView.as_view(),
    #      name='logout'),

]