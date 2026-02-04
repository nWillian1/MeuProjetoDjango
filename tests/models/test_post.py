import pytest # Importa o pytest para escrever testes
from blog.factories.factories import PostFactory # Ele busca da pasta que você criará no passo 3

@pytest.fixture # Define um fixture do pytest para criar um post publicado
def post_published():  # Nome do fixture
    return PostFactory(title='pytest with factory') # Cria o dado fictício

@pytest.mark.django_db # Permite que o teste use o seu banco de dados
def test_create_published_post(post_published): # O teste recebe o fixture como argumento
    assert post_published.title == 'pytest with factory' # A "prova real"