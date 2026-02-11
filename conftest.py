import os # Importa o módulo os para manipulação de variáveis de ambiente
import django # Importa o módulo django para configurar o ambiente Django

def pytest_configure(): # Função de configuração do pytest para Django
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "setup.settings") # Define a variável de ambiente para o módulo de configurações do Django
    django.setup()# Configura o ambiente Django para que os testes possam ser executados corretamente
