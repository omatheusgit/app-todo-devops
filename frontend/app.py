import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Configurações iniciais
load_dotenv()
API_URL = os.getenv('API_URL')

st.set_page_config(page_title="Tarefas ToDo", layout="wide")
st.title("📝 Gerenciador de Tarefas To-Do")

# Função para buscar todas as tarefas
def buscar_tarefas():
    try:
        response = requests.get(API_URL)
        tarefas = []
        if response.status_code == 200:
            dados = response.json()

            for tarefa in dados:
                tarefas.append({
                    "id": tarefa.get("id"),
                    "ANDAMENTO": tarefa.get("concluida"),
                    "TITULO": tarefa.get("titulo"),
                    "DESCRIÇÃO": tarefa.get("descricao"),
                    "CONCLUSÃO PREVISTA": tarefa.get("data_criacao"),
                    "DATA CONCLUSÃO": tarefa.get("data_conclusao"),
                    
                })
            
            return tarefas

        else:
            st.error("Erro ao buscar tarefas.")
            return []
    except Exception as e:
        st.error(f"Erro: {e}")
        return []

# Criar nova tarefa
with st.expander("➕ Criar nova tarefa"):
    titulo = st.text_input("Título")
    descricao = st.text_area("Descrição")
    if st.button("Salvar tarefa"):
        if titulo and descricao:
            payload = {"titulo": titulo, "descricao": descricao}
            try:
                res = requests.post(API_URL, json=payload)
                if res.status_code == 201:
                    st.success("Tarefa criada com sucesso!")
                    st.rerun()
                else:
                    st.error("Erro ao criar tarefa.")
            except Exception as e:
                st.error(f"Erro: {e}")
        else:
            st.warning("Preencha todos os campos.")

# Mostrar tarefas
st.subheader("📋 Tarefas registradas")
tarefas = buscar_tarefas()

if tarefas:
    st.table(tarefas)
else:
    st.info("Nenhuma tarefa encontrada.")
