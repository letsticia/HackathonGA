import matplotlib.pyplot as plt
import streamlit as st
import numpy as np

def planoCartesiano(pontoA_x, pontoA_y, pontoB_x, pontoB_y, distancia = None, media = None, reta = None):
    """Função para plotar um plano cartesiano com dois pontos A e B e, opcionalmente, a distância entre eles, a média deles e a equação da reta que passa por eles.

    Args:
    pontoA_x (int): Coordenada x do ponto A.
    pontoA_y (int): Coordenada y do ponto A.
    pontoB_x (int): Coordenada x do ponto B.
    pontoB_y (int): Coordenada y do ponto B.
    distancia (bool, optional): Se True, exibe a distância entre os pontos A e B. Defaults to None.
    media (bool, optional): Se True, exibe a média dos pontos A e B. Defaults to None.
    reta (bool, optional): Se True, exibe a equação da reta que passa pelos pontos A e B. Defaults to None.
    """
    
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
    
def pontos():
    """Função para exibir a interface da funcionalidade de pontos.
    """
    
    st.subheader("Pontos")
    st.write("Aqui você pode calcular a distância entre dois pontos, a média de dois pontos e a equação da reta que passa por dois pontos.")
    
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

def planoCartesianoReta(reta_a, reta_b, c, ponto_x = None, ponto_y = None, distancia = None):
    
    ponto = (ponto_x, ponto_y)
    
    # Criando a figura e o eixo
    fig, ax = plt.subplots()
    
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

    if distancia:
        division = reta_a**2 + reta_b**2
        
        if division == 0:
            st.error("A equação da reta não é válida.")
        else:
            distancia = abs(reta_a * ponto_x + reta_b * ponto_y + c) / (reta_a**2 + reta_b**2)**0.5
            
            if distancia.is_integer():
                distancia = int(distancia)
                st.info(f"A distância do ponto ({ponto_x}, {ponto_y}) à reta {reta_a}x + {reta_b}y + {c} = 0 é {distancia}.")
            else:
                st.info(f"A distância do ponto ({ponto_x}, {ponto_y}) à reta {reta_a}x + {reta_b}y + {c} = 0 é {distancia:.2f}.")
            
            # Plotando o ponto
            ponto = (ponto_x, ponto_y)
            ax.plot(*ponto, 'ro', markersize = 5)
            ax.annotate(f'P{ponto_x, ponto_y}', ponto, textcoords="offset points", xytext=(-15,-15), ha='center', color='red')
            
            # Calculando o valor absoluto máximo entre as coordenadas x e y do ponto
            max_value = max(abs(ponto_x), abs(ponto_y))
            
            # Definindo os limites dos eixos
            ax.set_xlim(-max_value-10, max_value+10)
            ax.set_ylim(-max_value-10, max_value+10)
            
            # Desenhando linhas tracejadas do eixo x até o ponto e do eixo y até o ponto
            ax.hlines(ponto_y, 0, ponto_x, colors='red', linestyles='dashed', linewidth=0.5)
            ax.vlines(ponto_x, 0, ponto_y, colors='red', linestyles='dashed', linewidth=0.5)
            
            x_values = np.linspace(-max_value-10, max_value+10, 400)
            y_values = (-reta_a * x_values - c) / reta_b
            ax.plot(x_values, y_values, 'g-', linewidth = 1)
            
            # Exibindo a grade
            ax.grid(True)

            # Exibindo o gráfico no Streamlit
            st.pyplot(fig)
                    

    
        
        
            
        
    
   
def retas():
    """Função para exibir a interface da funcionalidade de retas.
    """
    
    st.subheader("Retas")
    st.write("Aqui você pode calcular: a distância de um ponto a uma reta e a equação da reta paralela ou perpendicular a uma reta dada que passa por um ponto.")
    opcao = st.radio("Selecione uma opção:", ["Distância de um ponto a uma reta", "Equação da reta paralela ou perpendicular a uma reta dada que passa por um ponto"])
    
    if opcao == "Distância de um ponto a uma reta":
        
        st.info("1. Para calcular a distância de um ponto a uma reta, você precisa da equação da reta e das coordenadas do ponto.")
        st.info("2. Aqui, consideramos a equação da reta na forma (ax + by + c = 0)")
        st.info("3. A distância de um ponto (x0, y0) a uma reta ax + by + c = 0 é dada pela fórmula: d = $\\frac{|ax + by + c|}{\\sqrt{a^2 + b^2}}$, onde d é a distância.")
        
        ponto_x = st.number_input("Digite a coordenada x do ponto:", value=0)
        ponto_y = st.number_input("Digite a coordenada y do ponto:", value=0)
        
        reta_a = st.number_input("Digite o coeficiente angular da reta (a):", value=0)
        reta_b = st.number_input("Digite o coeficiente linear da reta (b):", value=0)
        reta_c = st.number_input("Digite o termo independente da reta (c):", value=0)
        
        planoCartesianoReta(reta_a, reta_b, reta_c, ponto_x, ponto_y, distancia = True)
        
        
        
        
            
        # exibindo o gráfico
        
        
        