import streamlit as st
import matplotlib.pyplot as plt
from utils.utils import planoCartesiano

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

st.write("Este aplicativo tem como objetivo facilitar o cálculo de pontos, retas, circunferências, volumes e áreas, e vetores na Geometria Analítica.")

funcionalidade = st.radio("Selecione um dos assuntos:", ["Pontos", "Retas", "Circunferências", "Volumes e Áreas", "Vetores"])

if funcionalidade == "Pontos":
    st.subheader("Pontos")
    st.write("Aqui você pode calcular a distância entre dois pontos, a média de dois pontos, a equação da reta que passa por dois pontos, e a equação da circunferência com centro em um ponto e raio r.")
    
    pontoA_x = st.number_input("Digite a coordenada x do ponto A:", value=0)
    pontoA_y = st.number_input("Digite a coordenada y do ponto A:", value=0)
    
    pontoB_x = st.number_input("Digite a coordenada x do ponto B:", value=0)
    pontoB_y = st.number_input("Digite a coordenada y do ponto B:", value=0)
    

    st.write("O que você deseja Fazer?")
    opcao = st.radio("Selecione uma opção:", ["Exibir Pontos", "Distância entre dois pontos", "Média de dois pontos", "Equação da reta que passa por dois pontos"])
    
    
    if opcao == "Exibir Pontos":
        planoCartesiano(pontoA_x, pontoA_y, pontoB_x, pontoB_y)
    elif opcao == "Distância entre dois pontos":
        planoCartesiano(pontoA_x, pontoA_y, pontoB_x, pontoB_y, distancia = True)
    elif opcao == "Média de dois pontos":
        planoCartesiano(pontoA_x, pontoA_y, pontoB_x, pontoB_y, media = True)
    elif opcao == "Equação da reta que passa por dois pontos":
        planoCartesiano(pontoA_x, pontoA_y, pontoB_x, pontoB_y, reta = True)
    
    
    