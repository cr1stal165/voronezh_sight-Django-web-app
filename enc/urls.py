"""enc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from enc_vrn import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('add_sight/', views.add_sight, name="add_sight"),
    path('add_excursion/', views.add_excursion, name="add_excursion"),
    path('show_sight/<int:sight_id>,<int:his_id>', views.show_sight, name="show_sight"),
    path('confirm_add_sight/', views.confirm_add_sight, name="confirm_add_sight"),
    path('delete_sight/<int:sight_id>,<int:his_id>', views.delete_sight, name="delete_sight"),
    path('edit_sight/<int:sight_id>,<int:his_id>', views.edit_sight, name="edit_sight"),
    path('confirm_edit_sight/<int:sight_id>,<int:his_id>', views.confirm_edit_sight, name="confirm_edit_sight"),
    path('show_excursion/', views.show_excursion, name="show_excursion"),
    path('show_architectors/', views.show_architectors, name="show_architectors"),
]


if settings.DEBUG:
    urlpatterns += static(
            settings.STATIC_URL,
            document_root=settings.STATIC_ROOT
    ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
