##  Progresso do Projeto - Módulo de Blog

###  Modelagem de Dados
- Criado o modelo `Post` com campos para título, autor (relacionado ao User padrão do Django), conteúdo, data de criação e slug.
- Migrações aplicadas com sucesso para estruturar o banco de dados SQLite.
- Testes manuais realizados via Django Shell para criação e filtragem de objetos.

###  Testes Automatizados
- Configuração do ambiente de testes utilizando **Pytest**.
- Implementação de **Factories** com a biblioteca `factory_boy` e `faker` para geração de dados fictícios e escaláveis.
- Criação de testes de modelo para garantir a integridade da criação de posts.

## Interface Administrativa
- Sistema de administração nativa do Django para gerenciamento de conteúdo

## Como acessar
- 1º Com o servidor rodando (`python manage.py runserver`), acesse: `http://127.0.0.1:8000/admin/`.
- 2º Utilize as credenciais de superusuário criadas durante o desenvolvimento.

## Modelos Registrados
- O modelo `Post` (localizado em `./blog/Models/post.py`) está totalmente integrado ao painel, permitindo operações de criação, leitura, atualização e exclusão

**Como rodar os testes:**
```bash
pytest