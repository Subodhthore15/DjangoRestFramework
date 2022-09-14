from django.contrib import admin
from django.urls import path,include

from .views import *
urlpatterns = [
    
    path('get-todo/',todo_get),
    path('post-todo/',todo_post),
    
    path('get-todo/<int:pk>',todo_get_pk),
    path('update-todo/<int:pk>',todo_update_pk),
    path('delete-todo/<int:pk>',todo_delete_pk),
    
]
