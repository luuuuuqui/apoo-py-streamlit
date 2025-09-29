from templates.manteritemUI import ManterItemUI
import streamlit as st

class IndexUI:
    @staticmethod
    def menu_admin():            
        ManterItemUI.main()

    @staticmethod
    def sidebar():
        IndexUI.menu_admin()

    @staticmethod
    def main():
        IndexUI.sidebar()

if __name__ == "__main__":
    ManterItemUI.main()