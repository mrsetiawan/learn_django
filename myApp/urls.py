from django.contrib import admin
from django.urls import path

from . import views as mainApp
from myBlog import views as blog
from myAbout import views as about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', mainApp.index),
    path('blog/', blog.index),
    path('about/', about.index)
]
