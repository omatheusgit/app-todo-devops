# 📝 Projeto: Gerenciador de Tarefas To-Do (Fullstack com Docker + Flask + Streamlit)

Esse projeto é um desafio pessoal com foco em DevOps, pra montar um portfólio prático e funcional, que abrange desde o backend até o frontend — tudo containerizado e pronto pra subir com um `docker compose up`.

---

## 🚀 Por que esse projeto?

A ideia aqui foi sair da teoria e colocar em prática várias etapas que envolvem um ambiente real de desenvolvimento e deploy.

Criei esse To-Do simples com objetivo de:

- praticar estrutura de microsserviços (back + front isolados)
- trabalhar com banco de dados
- integrar variáveis de ambiente (`.env`)
- empacotar com Docker
- orquestrar com Docker Compose
- contruir as aplicações em Kubernetes de forma declarativa (`yaml`)
- build e push das imagens no Docker Hub (`ci`)
- deploy automatizado no cluster Kubernetes em cloud (`cd`)

---

## ⚙️ O que foi usado

O projeto foi dividido em dois serviços principais:

### 💡 Frontend

- **Streamlit** para visualização e controle das tarefas
- Tela única com abas para listar, editar, criar e excluir tarefas
- Comunicação com a API via `requests`

### 🧠 Backend

- **Flask** com estrutura modular (blueprints)
- Banco de dados **SQLite** usando SQLAlchemy
- Documentação automática com **Flasgger** acessível via `/docs`
- Variáveis de ambiente via `python-dotenv`
- Roteamento completo para CRUD de tarefas


### 🏗️ Infraestrutura

- Dockerfile separado para frontend e backend
- `.env` isolados para frontend e backend
- Compose para orquestrar tudo com 1 comando

---

### 🚢 CI/CD com GitHub Actions e Kubernetes

A pipeline CI/CD automatiza todo o processo com GitHub Actions:

- **CI**: Ao criar uma tag (`vX.Y.Z`), as imagens do backend e frontend são construídas e enviadas ao Docker Hub.
- **CD**: Após o build, os manifestos YAML são aplicados no cluster Kubernetes da DigitalOcean, atualizando o deploy com a nova versão.
- **Segurança**: Toda autenticação é feita via secrets (`DOCKERHUB_TOKEN` e `KUBE_CONFIG`).
- **Extra**: Há um job opcional para destruir os recursos criados com aprovação manual.

---

## 🧠 Como funciona?

![Tela do Streamlit](images/interface-streamlit.png)
*Interface do frontend feita em Streamlit, com abas para listar, editar e excluir tarefas.*

![Interface da API Swagger](images/api-docs.png)
*Documentação da API Flask gerada automaticamente com Flasgger, acessível em `/docs`.*

A interface web em Streamlit se conecta com a API Flask para realizar operações de:

- criar nova tarefa
- visualizar todas as tarefas
- editar tarefa existente
- excluir tarefa pelo ID
- marcar/desmarcar como concluída

Tudo isso usando o banco SQLite embarcado e com persistência garantida via volume (se quiser).

A API conta ainda com documentação interativa acessando `http://localhost:5000/docs`.

---

## 🐳 Como rodar o projeto?

Simples. Após clonar:

```bash
docker compose up --build
```

Tudo já configurado pra rodar de primeira, desde que tenha Docker e Docker Compose instalados.

---

## 📚 Stacks e conhecimentos aplicados

- Python 3.12
- Flask
- Streamlit
- SQLAlchemy
- Docker
- Docker Compose
- Kubernetes (DigitalOcean)
- GitHub Actions (CI/CD)
- Arquitetura de microsserviços
- Manipulação de variáveis com `.env`
- Criação e consumo de API REST
- Modularização de projetos em Flask
- YAML para infraestrutura declarativa
- Markdown, documentação e boas práticas

---

## 🔄 Em desenvolvimento

- Testes automatizados
- Ajustes visuais no frontend
- Refinamento do código

---

Projeto de gaveta que veio de uma ideia para automatizar rotina? Talvez.  
Portfólio prático e que mostra conhecimento? Com certeza.

💻 Bora codar e evoluir sempre.
