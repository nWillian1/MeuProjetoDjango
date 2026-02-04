## 🚀 Progresso do Projeto - Módulo de Blog

### 📝 Modelagem de Dados
- Criado o modelo `Post` com campos para título, autor (relacionado ao User padrão do Django), conteúdo, data de criação e slug.
- Migrações aplicadas com sucesso para estruturar o banco de dados SQLite.
- Testes manuais realizados via Django Shell para criação e filtragem de objetos.

### 🧪 Testes Automatizados
- Configuração do ambiente de testes utilizando **Pytest**.
- Implementação de **Factories** com a biblioteca `factory_boy` e `faker` para geração de dados fictícios e escaláveis.
- Criação de testes de modelo para garantir a integridade da criação de posts.

**Como rodar os testes:**
```bash
pytest