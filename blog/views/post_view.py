from django.http import HttpResponse # Importando HttpResponse
from django.views import generic # Importando visualizações genéricas

class PostViews(generic.View): # Criando uma visualização genérica
    def get(self, request, *args, **kwargs): # Definindo o método GET
        return HttpResponse("Hello World") # Retornando uma resposta HTTP simples