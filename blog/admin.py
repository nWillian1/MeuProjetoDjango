from django.contrib import admin

# Register your models here.

from .Models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'created_on', 'status') # Campos a serem exibidos na lista de posts
    list_filter = ('status', 'created_on') # Filtros para status e data de criação
    search_fields = ['title', 'content'] # Campos para pesquisa
    prepopulated_fields = {'slug': ('title',)} # Gerar automaticamente o slug a partir do título


admin.site.register(Post, PostAdmin) # Registrando o modelo Post no admin do Django com a configuração personalizada PostAdmin