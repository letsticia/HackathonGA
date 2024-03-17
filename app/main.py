import streamlit as st
import matplotlib.pyplot as plt
from utils.utils import pontos, retas, circunferencias

st.set_page_config(
    page_title="Calculadora de Geometria Analítica",
    page_icon="📐",
    initial_sidebar_state="collapsed",
    menu_items={
        "Get help": None,
        "Report a bug": None,
        "About": None,
    }
)

st.header("Calculadora de Geometria Analítica")

st.write("Este aplicativo tem como objetivo facilitar o cálculo de pontos, retas e circunferências na Geometria Analítica.")

funcionalidade = st.radio("Selecione um dos assuntos:", ["Pontos", "Retas", "Circunferências"])

if funcionalidade == "Pontos":
    pontos()
elif funcionalidade == "Retas":
    retas()
elif funcionalidade == "Circunferências":
    circunferencias()