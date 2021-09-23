from django.urls import path

from core.views import indexView, articleView

app_name = 'blog'

urlpatterns = [
    path('', indexView, name='index'),
    path('article/<slug:slug>', articleView, name='article'),
]
