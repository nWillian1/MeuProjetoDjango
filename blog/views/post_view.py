from django.views import generic # Importando visualizações genéricas

from blog.Models import Post # Importando o modelo Post a partir da pasta blog e do arquivo Models.py

class PostViews(generic.ListView): # Criando uma visualização genérica de lista
    queryset = Post.objects.all().order_by('-created_on') # Definindo a consulta para obter os posts publicados, ordenados por data de criação
    template_name = 'index.html' # Especificando o template a ser usado para renderizar a visualização

class PostDetail(generic.DetailView): # Criando uma visualização genérica de detalhes
    model = Post # Especificando o modelo a ser usado para esta visualização
    template_name = 'post_detail.html' # Especificando o template a ser usado para renderizar a visualização