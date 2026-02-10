from django.db import models # Importando modelos de Django
from django.contrib.auth.models import User # Importando modelo de usuario de Django

STATUS = ( # Definindo opções de status para o post
    (0, 'Draft'), # Rascunho
    (1, 'Published'), # Publicado
)

class Post(models.Model): # Definindo o modelo Post
    title = models.CharField(max_length=200, unique=True) # Título do post
    slug = models.SlugField(max_length=200, unique=True) # Slug do post (aceita texto ou carcteres especiais)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts') # Autor do post
    updated_on = models.DateTimeField(auto_now=True) # Data de atualização do post
    content = models.TextField() # Conteúdo do post
    created_on = models.DateTimeField(auto_now_add=True) # Data de criação do post
    status = models.IntegerField(choices=STATUS, default=0) # Status do post

    class Meta: # Metadados do modelo
        ordering = ['-created_on'] # Ordenação padrão por data de criação decrescente

    def __str__(self): # Representação em string do modelo
        return self.title # Retorna o título do post
    