from django.urls import path, include
from .views import Auth_github, Auth_google, home, profile, signin, signup, user_dashboard, LogOut
from django.contrib.auth.views import LogoutView


urlpatterns = [ 
    path('accounts/', include('allauth.urls')),
    path('accounts/', Auth_github, name='github'),
    path('accounts/', Auth_google, name='google'),
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('dashboard/', user_dashboard, name='dashboard'),
    path('profile/', profile, name='profile'),
    path('logout/', LogOut, name='logout')

]
 