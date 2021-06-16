
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("home.urls")),
    path('accounts/', include('allauth.urls'))

]
handler400 = 'home.views.error_400_view'
handler404 = 'home.views.error_404_view'
handler500 = 'home.views.error_500_view'
handler403 = 'home.views.error_403_view'
