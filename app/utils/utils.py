import matplotlib.pyplot as plt
import streamlit as st
import numpy as np

def planoCartesiano(pontoA_x, pontoA_y, pontoB_x, pontoB_y, distancia = None, media = None, reta = None):
    
    pontoA = (pontoA_x, pontoA_y)
    pontoB = (pontoB_x, pontoB_y)
    
     # Criando a figura e o eixo
    fig, ax = plt.subplots()

    # Plotando os pontos
    ax.plot(*pontoA, 'ro', markersize = 5)  # Ponto A em vermelho
    ax.plot(*pontoB, 'bo', markersize = 5)  # Ponto B em azul
    
    # Calculando o valor absoluto máximo entre as coordenadas x e y dos pontos
    max_value = max(abs(pontoA_x), abs(pontoA_y), abs(pontoB_x), abs(pontoB_y))
    
    if distancia:
        distancia = ((pontoB_x - pontoA_x)**2 + (pontoB_y - pontoA_y)**2)**0.5
        st.info(f"A distância entre os pontos A e B é {distancia:.2f}.")
        ax.plot([pontoA_x, pontoB_x], [pontoA_y, pontoB_y], 'g-', linewidth = 1)  # Linha verde tracejada entre os pontos A e B
    elif media:
        media_x = (pontoA_x + pontoB_x) / 2
        media_y = (pontoA_y + pontoB_y) / 2
        
        if media_x.is_integer() and media_y.is_integer():
            media_x = int(media_x)
            media_y = int(media_y)
            st.info(f"A média dos pontos A e B é ({media_x}, {media_y}) representado por C no plano cartesiano.")
        elif media_x.is_integer():
            media_x = int(media_x)
            st.info(f"A média dos pontos A e B é ({media_x}, {media_y:.2f}) representado por C no plano cartesiano.")
        elif media_y.is_integer():
            media_y = int(media_y)
            st.info(f"A média dos pontos A e B é ({media_x:.2f}, {media_y}) representado por C no plano cartesiano.")
        else:
            st.info(f"A média dos pontos A e B é ({media_x:.2f}, {media_y:.2f}) representado por C no plano cartesiano.")    
        
        pontoC = (media_x, media_y)
        
        ax.plot(*pontoC, 'go', markersize = 5)
        
        ax.hlines(media_y, 0, media_x, colors='green', linestyles='dashed', linewidth=0.5)
        ax.vlines(media_x, 0, media_y, colors='green', linestyles='dashed', linewidth=0.5)
        ax.annotate(f'C{media_x, media_y}', pontoC, textcoords="offset points", xytext=(-15,-15), ha='center', color='green', bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.2'))
    elif reta:
        
        division = pontoB_x - pontoA_x
        
        if division == 0:
            st.info(f"A equação da reta que passa pelos pontos A e B é x = {pontoA_x}.")
            x = [pontoA_x, pontoB_x]
            y = [pontoA_y, pontoB_y]
            ax.plot(x, y, 'g-', linewidth = 1)
        else:
            m = (pontoB_y - pontoA_y) / (pontoB_x - pontoA_x)
            b = pontoA_y - m * pontoA_x
            
            if m.is_integer and b.is_integer():
                m = int(m)
                b = int(b)
                st.info(f"A equação da reta que passa pelos pontos A e B é y = {m}x + {b}.")
            elif m.is_integer():
                m = int(m)
                st.info(f"A equação da reta que passa pelos pontos A e B é y = {m}x + {b:.2f}.")
            elif b.is_integer():
                b = int(b)
                st.info(f"A equação da reta que passa pelos pontos A e B é y = {m:.2f}x + {b}.")
            else:
                st.info(f"A equação da reta que passa pelos pontos A e B é y = {m:.2f}x + {b:.2f}.")
            
        
        # Definindo os valores de x para cobrir todo o intervalo do gráfico
        x_values = np.linspace(-max_value-10, max_value+10, 400)

        # Calculando os valores de y
        y_values = m * x_values + b

        # Plotando a reta
        ax.plot(x_values, y_values, 'g-', linewidth = 1)
           
    
    
    # Desenhando linhas tracejadas do eixo x até o ponto e do eixo y até o ponto
    ax.hlines(pontoA_y, 0, pontoA_x, colors='red', linestyles='dashed', linewidth=0.5)
    ax.vlines(pontoA_x, 0, pontoA_y, colors='red', linestyles='dashed', linewidth=0.5)

    ax.hlines(pontoB_y, 0, pontoB_x, colors='blue', linestyles='dashed', linewidth=0.5)
    ax.vlines(pontoB_x, 0, pontoB_y, colors='blue', linestyles='dashed', linewidth=0.5)

    if pontoA_x != 0 and pontoA_y != 0:
        ax.annotate(f'A{pontoA_x, pontoA_y}', pontoA, textcoords="offset points", xytext=(-15,-15), ha='center', color='red')
    
    if pontoB_x != 0 and pontoB_y != 0:
        ax.annotate(f'B{pontoB_x, pontoB_y}', pontoB, textcoords="offset points", xytext=(-15,-15), ha='center', color='blue')

    # Movendo as espinhas para o centro
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    # Movendo os ticks para o centro
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    
    ax.axhline(0, color='black',linewidth=0.5)
    ax.axvline(0, color='black',linewidth=0.5)

    # Definindo os limites dos eixos
    ax.set_xlim(-max_value-10, max_value+10)
    ax.set_ylim(-max_value-10, max_value+10)
    
    # Exibindo a grade
    ax.grid(True)

    # Exibindo o gráfico no Streamlit
    st.pyplot(fig)