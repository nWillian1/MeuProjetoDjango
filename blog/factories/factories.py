import factory # Importa a biblioteca factory_boy para criar fábricas
from faker import Factory as FakerFactory # Importa a biblioteca Faker para gerar dados fictícios, como nomes e e-mails

from django.contrib.auth.models import User # Importa o modelo User do Django para criar usuários fictícios
from django.utils.timezone import now # Importa a função now para definir a data de criação dos posts

from blog.Models import Post # Importa o modelo Post do seu aplicativo blog para criar posts fictícios

faker = FakerFactory.create() # Cria uma instância do Faker para gerar dados fictícios, como nomes e e-mails


class UserFactory(factory.django.DjangoModelFactory): # Define uma fábrica para criar usuários fictícios
    class Meta: # Define a meta classe para a fábrica
        model = User # Especifica que esta fábrica cria instâncias do modelo User

    email = factory.Faker("safe_email") # Gera um e-mail fictício usando Faker
    username = factory.LazyAttribute(lambda x: faker.name()) # Gera um nome de usuário fictício usando Faker


    @classmethod # Define um método de classe para preparar o usuário antes de salvá-lo
    def _prepare(cls, create, **kwargs): # Sobrescreve o método _prepare para definir a senha corretamente
        password = kwargs.pop("password", None) # Remove a senha dos argumentos, se fornecida
        user = super(UserFactory, cls)._prepare(create, **kwargs) # Chama o método _prepare da superclasse para criar o usuário
        if password: # Se uma senha foi fornecida
            user.set_password(password) # Define a senha do usuário corretamente usando o método set_password
            if create: # Se o usuário deve ser salvo no banco de dados
                user.save() # Salva o usuário no banco de dados
            return user # Retorna a instância do usuário criado
        
class PostFactory(factory.django.DjangoModelFactory): # Define uma fábrica para criar posts fictícios
    title = factory.LazyAttribute(lambda x: faker.sentence()) # Gera um título fictício usando Faker
    created_on = factory.LazyAttribute(lambda x: now()) # Define a data de criação do post como a data e hora atual
    author = factory.SubFactory(UserFactory) # Cria um autor fictício usando a fábrica UserFactory
    status = 0


    class Meta: # Define a meta classe para a fábrica
        model = Post # Especifica que esta fábrica cria instâncias do modelo Post