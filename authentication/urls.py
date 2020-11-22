from django.conf.urls import url
from django.urls import path, include
from .views import RegisterView
from .views import LoginView


urlpatterns = [
      path('register/', RegisterView.as_view()),
      path('logout/', LogoutView.as_view(), name='auth_logout'),
      path('logout_all/', LogoutAllView.as_view(), name='auth_logout_all'),
     
]

