import streamlit as st
import requests
import os
import pandas as pd
from datetime import datetime
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
    titulo = st.text_input("Título", key="titulo")
    descricao = st.text_area("Descrição", key="descricao")
    data = st.date_input("Data da tarefa")
    hora = st.time_input("Hora da tarefa")
    
    if st.button("Salvar tarefa"):
        
        if not titulo or not descricao:
            st.warning("Preencha todos os campos.")
        
        else:
            data_criacao = datetime.combine(data, hora)
            payload = {
                "titulo": titulo, 
                "descricao": descricao,
                "data_criacao": data_criacao.strftime("%Y-%m-%d %H:%M")

            }

            try:
                response = requests.post(API_URL, json=payload)
                if response.status_code == 201:
                    st.success("Tarefa criada com sucesso!")
                    # st.rerun()
                else:
                    st.error("Erro ao criar tarefa.")
            except Exception as e:
                st.error(f"Erro: {e}")

# Mostrar tarefas
st.subheader("📋 Tarefas registradas")
tarefas = buscar_tarefas()

if tarefas:
    # remover indice do componente
    df = pd.DataFrame(tarefas)
    df.reset_index(drop=True, inplace=True)
    st.dataframe(df, hide_index=True)
else:
    st.info("Nenhuma tarefa encontrada.")
    
