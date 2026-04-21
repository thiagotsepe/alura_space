# 🚀 Alura Space — Galeria de Fotos do Espaço

Projeto desenvolvido durante o aprendizado de Django, construindo uma galeria de fotografias astronômicas com funcionalidades de listagem, filtro por categoria, busca e autenticação de usuários.

---
# 📚 Sobre o Projeto

O Alura Space é uma aplicação web que exibe uma galeria de fotos do espaço (nebulosas, estrelas, galáxias e planetas), permitindo ao usuário navegar, filtrar por categoria e buscar imagens pelo nome.
O foco do projeto é o aprendizado prático do framework Django, cobrindo desde a criação de models e autenticação de usuários até o roteamento de URLs e renderização de templates.

---
# ✨ Funcionalidades

### 🖼️ Galeria
- Listagem de fotografias cadastradas
- Filtro por categoria (Nebulosa, Estrela, Galáxia, Planeta)
- Tag ativa com destaque visual ao filtrar
- Busca por nome de fotografia
- Página de detalhe de cada imagem
- Exibição apenas de fotos publicadas

### 🔐 Autenticação

- Cadastro de novos usuários
- Login e logout de usuários
- Feedback visual com mensagens flash (alerts) para ações do usuário

---
# 🛠️ Tecnologias Utilizadas

- Python 3.14
- Django 6.0
- HTML5 & CSS3
- Bootstrap 5
- SQLite (banco de dados padrão do Django)

---
# 📖 Conceitos Aprendidos
### Models & ORM

- Criação de models com choices/opções
- Uso do método get_FOO_display() para exibir valores legíveis
- Filtros no ORM Django (filter, icontains, order_by)

### Views & URLs

- Roteamento com urls.py e passagem de parâmetros
- Reutilização de templates entre views diferentes
- Passagem de contexto (context) do backend para o template
- Busca via query string com request.GET.get()

### Autenticação

- Uso do sistema de autenticação nativo do Django (django.contrib.auth)
- Criação de formulários de cadastro e login
- Uso de authenticate() e login() / logout()
- Proteção de rotas e redirecionamento pós-autenticação
- Sistema de mensagens com django.contrib.messages e renderização no template

### Templates

- Uso de {% url %}, {% if %}, {% for %} nos templates Django
- Arquivos estáticos com {% static %}
- Herança de templates com {% extends %} e {% block %}
- Inclusão de partials com {% include %}
- Exibição de mensagens flash com {% for message in messages %}

---
# 🚀 Como rodar o projeto

  ## Clone o repositório
  - git clone https://github.com/thiagotsepe/alura_space.git
  - cd alura_space
  
  ## Crie e ative um ambiente virtual
  - python -m venv venv
  - source venv/bin/activate / # Windows: venv\Scripts\activate
  
  ## Instale as dependências
  - pip install -r requirements.txt
  
  ## Rode as migrações
  - python manage.py migrate
  
  ## Inicie o servidor
  - python manage.py runserver
