# 🚀 Alura Space — Galeria de Fotos do Espaço

Projeto desenvolvido durante o aprendizado de **Django**, construindo uma galeria de fotografias astronômicas com funcionalidades de listagem, filtro por categoria e busca.

---

## 📚 Sobre o Projeto

O **Alura Space** é uma aplicação web que exibe uma galeria de fotos do espaço (nebulosas, estrelas, galáxias e planetas), permitindo ao usuário navegar, filtrar por categoria e buscar imagens pelo nome.

O foco do projeto é o aprendizado prático do framework Django, cobrindo desde a criação de models até o roteamento de URLs e renderização de templates.

---

## ✨ Funcionalidades

- Listagem de fotografias cadastradas
- Filtro por categoria (Nebulosa, Estrela, Galáxia, Planeta)
- Tag ativa com destaque visual ao filtrar
- Busca por nome de fotografia
- Página de detalhe de cada imagem
- Exibição apenas de fotos publicadas

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.14**
- **Django 6.0**
- **HTML5 & CSS3**
- **SQLite** (banco de dados padrão do Django)

---

## 📖 Conceitos Aprendidos

- Criação de **models** com choices/opções
- Uso do método `get_FOO_display()` para exibir valores legíveis
- Roteamento com `urls.py` e passagem de parâmetros
- Filtros no ORM Django (`filter`, `icontains`, `order_by`)
- Reutilização de templates entre views diferentes
- Passagem de contexto (`context`) do backend para o template
- Uso de `{% url %}`, `{% if %}`, `{% for %}` nos templates Django
- Arquivos estáticos com `{% static %}`
- Busca via query string com `request.GET.get()`
