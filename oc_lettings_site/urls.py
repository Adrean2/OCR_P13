from django.contrib import admin
from django.urls import path, include

import lettings.views
import profiles.views
from . import views

urlpatterns = [path('', views.index, name='index'),
               path('profiles/', include("profiles.urls")),
               path('lettings/', include("lettings.urls")),
               path('admin/', admin.site.urls), ]
