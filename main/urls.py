from django.urls import path
from . import views, auth
urlpatterns = [
    path('', views.index),
    path('index', views.index),
    path('wall', views.wall),
    path('message/new', views.message_new),
    path('message/<int:msg_id>/edit', views.message_edit), 
    path('message/<int:msg_id>/destroy', views.message_destroy), 
    path('comentario/new', views.comentario_new),
    path('comentario/<int:cmt_id>/edit', views.comentario_edit), 
    path('comentario/<int:cmt_id>/destroy', views.comentario_destroy),
    
    
    path('registro', auth.registro),
    path('login', auth.login),
    path('logout', auth.logout)
]
