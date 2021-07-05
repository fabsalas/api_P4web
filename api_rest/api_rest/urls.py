"""api_rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from api.Login.LoginAPI import LoginAPI
from django.contrib import admin
from django.urls import path

from api.Libro.libroAPI import LibroAPI

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #LIBRO
    path('api/v1/libro/select/', LibroAPI.as_view(), name='LibroAPI'), #URL GET
    path('api/v1/libro/create/', LibroAPI.as_view(), name='LibroAPI'), #URL POST
    path('api/v1/libro/update/<int:id>/', LibroAPI.as_view(), name='LibroAPI'), #URL PUT
    path('api/v1/libro/create/<int:id>/', LibroAPI.as_view(), name='LibroAPI'), #URL DELETE

    #LOGIN
    path('api/v1/login/', LoginAPI.as_view(), name='LoginAPI'), #URL POST
    path('api/v1/logout/', LoginAPI.as_view(), name='LoginAPI'), #URL POST
]
urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
