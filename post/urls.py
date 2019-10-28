from django.urls import path

from .views import create, detail, my_post, delete, update

app_name        = 'post'
urlpatterns     = [
    path('create/', create, name='create'),
    path('delete/<delete_id>', delete, name='delete'),
    path('update/<update_id>', update, name='update'),
    path('detail/<slug:slugInput>',detail, name='detail'),
    path('my_post/', my_post, name='my_post'),
]