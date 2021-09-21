from django.shortcuts import render, HttpResponse,redirect
from .decorators import login_required
from django.db import IntegrityError
from .models import  Comentario, Mensaje, User
from django.contrib import messages
import bcrypt

@login_required
def index(request):
    users = User.objects.all(),
    mensajes=Mensaje.objects.all().order_by('-created_at')
    context = {
        "users": users,
        "mensajes":mensajes
    }
    return render(request, 'wall.html', context)

def message_new(request):
    
    usuario_id=request.session['user']['id']
    mensaje=request.POST['mensaje']
    autor=User.objects.get(id=usuario_id)
    Mensaje.objects.create(texto=mensaje,autor=autor)
    if 'from' in request.POST:
        return redirect('/'+request.POST['from'])
    return redirect('/index')

def message_edit(request,msg_id):
    mensaje_t=Mensaje.objects.get(id=msg_id)
    mensaje_t.texto=request.POST['texto']
    print(f'id:{msg_id},m:{mensaje_t.texto}')
    mensaje_t.save()
    messages.success(request,'Mensaje modificado con exito.')
    return redirect('/wall')

#aca van los mensajes con sus comentarios
def wall(request):
    mensajes=Mensaje.objects.all().order_by('-created_at')
    context = {        
        "mensajes":mensajes
    }
    return render(request, 'wall.html', context)

    
def comentario_new(request):
    usuario_id=request.session['user']['id']
    mensaje_id=request.POST['mensaje_id']
    comentario=request.POST['comentario']
    autor=User.objects.get(id=usuario_id)
    msg=Mensaje.objects.get(id=mensaje_id)
    Comentario.objects.create(texto=comentario,autor=autor,mensaje=msg)
    return redirect('/wall')

def comentario_edit(request,cmt_id):
    target=Comentario.objects.get(id=cmt_id)
    target.texto=request.POST['texto']
    print(f'id:{cmt_id},m:{target.texto}')
    target.save()
    messages.success(request,'Comentario modificado con exito.')
    return redirect('/wall')

def comentario_destroy(request,cmt_id):
    target=Comentario.objects.get(id=cmt_id)
    target.delete()
    messages.success(request,'Comentario eliminado con exito.')
    return redirect('/wall')

def message_destroy(request,msg_id):
    target=Mensaje.objects.get(id=msg_id)
    target.delete()
    messages.success(request,'Mensaje eliminado con exito.')
    return redirect('/wall')