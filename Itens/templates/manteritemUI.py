import streamlit as st
import pandas as pd
from controller.views import View 
import time

class ManterItemUI:
    @staticmethod
    def main():
        st.header("Cadastro de Itens")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterItemUI.listar()
        with tab2: ManterItemUI.inserir()
        with tab3: ManterItemUI.atualizar()
        with tab4: ManterItemUI.excluir()

    @staticmethod
    def listar():
        itens = View.item_listar()
        if len(itens) == 0: st.write("Nenhum item cadastrado")
        else:
            list_dic = []
            for obj in itens: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df)

    @staticmethod
    def inserir():
        descricao = st.text_input("Informe a descrição")
        quantidade = st.number_input("Informe a quantidade", min_value=0, step=1)
        if st.button("Inserir"):
            View.item_inserir(descricao, int(quantidade))
            st.success("Item inserido com sucesso")
            time.sleep(1)
            st.rerun()

    @staticmethod
    def atualizar():
        itens = View.item_listar()
        if len(itens) == 0: st.write("Nenhum item cadastrado")
        else:
            op = st.selectbox("Atualização de Itens", itens, format_func=lambda x: str(x))
            if op is not None:
                descricao = st.text_input("Informe a nova descrição:", op.descricao)
                quantidade = st.number_input("Informe a nova quantidade:", min_value=0, step=1, value=int(op.quantidade))
                if st.button("Atualizar"):
                    id = op.id
                    View.item_atualizar(id, descricao, int(quantidade))
                    st.success("Item atualizado com sucesso")
                    time.sleep(1)
                    st.rerun()

    @staticmethod
    def excluir():
        itens = View.item_listar()
        if len(itens) == 0: st.write("Nenhum item cadastrado")
        else:
            op = st.selectbox("Exclusão de Itens", itens, format_func=lambda x: str(x))
            if op is not None and st.button("Excluir"):
                id = op.id
                View.item_excluir(id)
                st.success("Item excluído com sucesso")
                time.sleep(1)
                st.rerun()
