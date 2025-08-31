from django.contrib import admin
from django.urls import path
from  . import views

urlpatterns = [
    path('',views.login,name='login'),
    path('login', views.login, name='login'), 
    path('sign_up',views.sign,name='sign_up'),
    path('add_note',views.add_notes,name='add_note'),
    path('logout',views.logout,name='logout'),
    path('my_note',views.my_note,name='my_note'),
    path('delete/<int:pk>/', views.delete_note, name='delete_note'),
    path('edit_note/<int:pk>/',views.edit_note,name="edit_note"),
    path('update_pass',views.update_pass,name="update_pass"),
    path('update_profile',views.update_profile,name="update_profile"),
]