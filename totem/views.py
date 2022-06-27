from pdb import post_mortem

from django.shortcuts import render
from django.template import context
from django.views.decorators.csrf import csrf_exempt

from totem.forms import TotemForm
from totem.models import Totem
from django.contrib.auth import get_user_model


# Create your views here.


def index_totem(request):
    if request.method =="POST":
        forms = TotemForm(request.POST)
        if forms.is_valid():
            forms.save()
    
    contatos = Totem.objects.all()
    dados = {
        "contatos":contatos
    }
    return render(request,"index.html", context=dados)

def index_criacao(request):
    forms = TotemForm()
    dados = {
        "forms":forms
    }
    return render(request,"index_criacao.html",context=dados)

def index_contato(request, id_contato):
    contatos = Totem.objects.filter(id=id_contato).first()
    dados = {
        "contatos":contatos
    }
    return render(request, "index_contato.html", context=dados)

def update_contato(request, id_contato):
    contato = Totem.objects.filter(id=id_contato).first()
    if request.method == "POST":  
        contato.paciente =request.POST["paciente"]
        contato.senha =request.POST["senha"]
        contato.sala =request.POST["sala"]
       # contato.data =request.POST.get["data"]
        contato.save()
        contato = Totem.objects.all()
        dados = {
        "contato":contato
    }
        return render(request, "index.html", context=dados)

    dados = {
        "contato":contato
    }
    return render(request, "update_contato.html", context=dados)

def delete_contato(request,id_contato):   
    Totem.objects.filter(id=id_contato).delete()
    contatos = Totem.objects.all()
    dados = {
        "contatos":contatos
    }
<<<<<<< HEAD
    return render(request, "index.html", context=dados)
=======
    return render(request, "index.html", context=dados)
>>>>>>> 98b66c46b5f50ce209aada250ca878c2297a1fbc
