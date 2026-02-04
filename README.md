# 📦 Gerenciador de Produtos (CRUD)

![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109.0-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)


## 🚀 Sobre o Projeto

Este projeto é uma aplicação **Full Stack** que demonstra a implementação de um **CRUD** (Create, Read, Update, Delete) utilizando a moderna stack do **FastAPI**.

Diferente de APIs tradicionais que retornam apenas JSON, este projeto utiliza **Server-Side Rendering (SSR)** com **Jinja2** para entregar uma interface gráfica pronta e responsiva diretamente do servidor.

### Principais Funcionalidades
- **Cadastro de Produtos:** Adição dinâmica de itens com nome, preço e categoria.
- **Listagem em Tempo Real:** Tabela visual com formatação de moeda brasileira (R$).
- **Edição e Remoção:** Controle total sobre os dados do sistema.
- **Banco de Dados Automático:** Utiliza SQLite, dispensando instalações complexas de servidores.
- **Interface Responsiva:** Design limpo e moderno (CSS customizado).

---

## 🛠️ Tecnologias Utilizadas

O projeto foi desenvolvido utilizando as seguintes tecnologias:

- **[Python 3.12+](https://www.python.org/)** - Linguagem base.
- **[FastAPI](https://fastapi.tiangolo.com/)** - Framework web moderno e de alta performance.
- **[SQLAlchemy](https://www.sqlalchemy.org/)** - ORM para manipulação eficiente do banco de dados.
- **[Jinja2](https://jinja.palletsprojects.com/)** - Motor de templates para renderização do HTML.
- **HTML5 & CSS3** - Front-end estilizado manualmente (sem frameworks pesados).
- **Uvicorn** - Servidor ASGI para produção.

---

## 📂 Estrutura do Projeto

```text
gerenciador-produtos/
│
├── main.py            # Lógica principal (Rotas e Banco de Dados)
├── loja.db            # Banco de Dados (Gerado automaticamente)
│
├── templates/         # Arquivos HTML (Front-end)
│   └── index.html
│
├── static/            # Arquivos Estáticos (CSS, Imagens)
│   └── style.css
│
└── requirements.txt   # Lista de dependências
