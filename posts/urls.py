from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    # path('posts/create', views.create, name='create'),
    # path('posts/delete/<int:pk>', views.delete, name='delete'),
    # path('posts/update/<int:pk>', views.update, name='update'),
    path('posts/<slug:slug>', views.show, name='show'),
    path('about', views.about, name='about'),
    path('search', views.search, name='search'),
]

