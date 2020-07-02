from django.urls import path
from . import views


urlpatterns = [
    path('',views.articles, name='articles'),
    path('article_delete/<art_id>', views.delete, name='article_delete')
]