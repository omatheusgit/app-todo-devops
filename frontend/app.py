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
st.title("📝 Gerenciador de Tarefas To - Do")

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

with st.expander("✔️ Cadastrar nova tarefa"):
    with st.form("form_criar_tarefa"):
        titulo = st.text_input("Título", key="titulo_input")
        descricao = st.text_area("Descrição", key="descricao_input")
        data = st.date_input("Data da tarefa", key="data_input")
        hora = st.time_input("Hora da tarefa", key="hora_input")

        submit = st.form_submit_button("💾 Salvar tarefa")

        if submit:
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
                    else:
                        st.error("Erro ao criar tarefa.")
                except Exception as e:
                    st.error(f"Erro: {e}")


with st.expander("📋 Tarefas cadastradas", expanded=True):
    tarefas = buscar_tarefas()

    if tarefas:
        # oculta o indice do componente
        df = pd.DataFrame(tarefas)
        # df.drop(columns=["id"], inplace=True, errors="ignore")
        df.reset_index(drop=True, inplace=True)
        st.dataframe(df, hide_index=True, use_container_width=True)
        
    else:
        st.info("Nenhuma tarefa encontrada.")

    if st.button("🔄 Atualizar lista"):
        st.session_state["atualizar_lista"] = True

    # Se for a primeira vez ou se clicou em atualizar
    if "atualizar_lista" not in st.session_state or st.session_state["atualizar_lista"]:
        tarefas = buscar_tarefas()
        st.session_state["atualizar_lista"] = False  # Resetar depois de atualizar

with st.expander("✏️ Editar tarefa"):

    with st.form("form_busca_id"):
        id = st.text_input("ID da tarefa", key="id_editar")
        buscar = st.form_submit_button("🔍 Carregar tarefa")

    if buscar:
        if id.isdigit():
            try:
                response = requests.get(f"{API_URL}/{int(id)}")
                if response.status_code == 200:
                    st.session_state.dados_tarefa = response.json()
                    st.session_state.carregou = True
                else:
                    st.warning("Tarefa não encontrada.")
            except Exception as e:
                st.error(f"Erro ao buscar tarefa: {e}")
        else:
            st.warning("Digite apenas números no campo de ID.")

    if st.session_state.get("carregou") and st.session_state.get("dados_tarefa"):
        dados_tarefa = st.session_state.dados_tarefa

        with st.form("form_edicao", clear_on_submit=False):
            titulo_editado = st.text_input("Título", value=dados_tarefa["titulo"], key="titulo_edit")
            descricao_editada = st.text_area("Descrição", value=dados_tarefa["descricao"], key="descricao_edit")

            data_planejada = pd.to_datetime(dados_tarefa["data_criacao"])
            data_edit = st.date_input("Data planejada", value=data_planejada.date(), key="data_edit")
            hora_edit = st.time_input("Hora planejada", value=data_planejada.time(), key="hora_edit")

            concluida = st.checkbox("Concluída", value=dados_tarefa["concluida"], key="check_edit")

            submit = st.form_submit_button("💾 Salvar alterações")

            if submit:
                data_criacao = datetime.combine(data_edit, hora_edit)
                data_conclusao = datetime.now().strftime("%Y-%m-%d %H:%M") if concluida else None

                payload = {
                    "titulo": titulo_editado,
                    "descricao": descricao_editada,
                    "data_criacao": data_criacao.strftime("%Y-%m-%d %H:%M"),
                    "concluida": concluida,
                    "data_conclusao": data_conclusao
                }

                try:
                    res = requests.put(f"{API_URL}/{id}", json=payload)
                    if res.status_code == 200:
                        st.success("Tarefa atualizada com sucesso!")
                        st.session_state.carregou = False
                    else:
                        st.error("Erro ao atualizar tarefa.")
                except Exception as e:
                    st.error(f"Erro: {e}")

with st.expander("❌ Excluir tarefa"):
     with st.form("form_excluir"):
        id_excluir = st.text_input("ID da tarefa a ser excluída", key="id_excluir")
        confirmar_exclusao = st.form_submit_button("🗑️ Excluir")

        if confirmar_exclusao:
            if id_excluir.isdigit():
                try:
                    response = requests.delete(f"{API_URL}/{int(id_excluir)}")
                    if response.status_code == 200:
                        st.success("Tarefa excluída com sucesso!")
                    elif response.status_code == 404:
                        st.warning("Tarefa não encontrada.")
                    else:
                        st.error("Erro ao excluir tarefa.")
                except Exception as e:
                    st.error(f"Erro: {e}")
            else:
                st.warning("O ID precisa ser um número inteiro.")
