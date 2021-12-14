from django.urls import path

from .views import*

urlpatterns = [
    path('blog/', index, name='blog'),
    path('news/<slug:article>/', categories),
    path('', index),


]
