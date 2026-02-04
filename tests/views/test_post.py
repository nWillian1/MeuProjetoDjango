import pytest # Importando pytest para testes
from django.urls import reverse # Importando reverse para resolver URLs
from blog.views.post_view import PostViews  # Importando a visualização PostViews

@pytest.mark.django_db  # Marcando o teste para usar o banco de dados Django
def test_post_list_view(client): # Testando a visualização PostListView
    url = reverse('home')  # Resolvendo a URL para a visualização
    response = client.get(url)  # Fazendo uma requisição GET para a URL
    assert response.status_code == 200  # Verificando se o status da resposta é 200
    # assert "Posts" in response.content.decode() # Verificando se o conteúdo da resposta contém 'Posts'
    assert response.content == b"Hello World"  # Verificando se o conteúdo da resposta é "Hello World!"