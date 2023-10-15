from django.conf.urls.static import static
from AscendBank import settings

from . import views
from django.urls import path



urlpatterns = [
    path('', views.home,name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/', views.logout, name='logout'),
    path('data/',views.data,name='data'),






]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)