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


def planoCartesianoReta(reta_a = None, reta_b = None, c = None, ponto_x = None, ponto_y = None, distancia = None, paralela = None, perpendicular = None):
    """ Função para plotar um plano cartesiano com uma reta e, opcionalmente, um ponto e a distância entre eles. Além disso, verifica se duas retas são paralelas e calcula a equação da reta perpendicular.

    Args:
        reta_a (int, optional): Coeficiente angular da reta. Defaults to None.
        reta_b (int, optional): Coeficiente linear da reta. Defaults to None.
        c (int, optional): Termo independente da reta. Defaults to None.
        ponto_x (int, optional): Coordenada x do ponto. Defaults to None.
        ponto_y (int, optional): Coordenada y do ponto. Defaults to None.
        distancia (bool, optional): Se True, exibe a distância entre o ponto e a reta. Defaults to None.
        paralela (bool, optional): Se True, verifica se duas retas são paralelas. Defaults to None.
        perpendicular (bool, optional): Se True, calcula a equação da reta perpendicular. Defaults to None.
    """
    
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
        ponto = (ponto_x, ponto_y)
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
            
    elif paralela:
        
        reta1_a = st.number_input("Digite o coeficiente angular da reta 1 (m1):", value=0)
        reta1_c = st.number_input("Digite o termo independente da reta 1 (c1):", value=0)
        
        reta2_a = st.number_input("Digite o coeficiente angular da reta 2 (m2):", value=0)
        reta2_c = st.number_input("Digite o termo independente da reta 2 (c2):", value=0)
        
        if reta1_a == reta2_a:
            st.info("As retas são paralelas.")
        else:
            st.info("As retas não são paralelas.")
        
        # Definindo os limites dos eixos
        ax.set_xlim(-10, 10)
        ax.set_ylim(-10, 10)
        
        # Definindo os valores de x para cobrir todo o intervalo do gráfico
        x_values = np.linspace(-10, 10, 400)
        y_values1 = reta1_a * x_values + reta1_c
        y_values2 = reta2_a * x_values + reta2_c
        
        # Plotando as retas
        ax.plot(x_values, y_values1, 'r-', linewidth = 1)
        ax.plot(x_values, y_values2, 'b-', linewidth = 1)
    
    elif perpendicular:
        
        reta_a = st.number_input("Digite o coeficiente angular da reta (m):", value=0)
        reta_c = st.number_input("Digite o termo independente da reta (c):", value=0)
        
        if reta_a == 0:
            reta_a = 0.0001
        
        fracao = f"y = -\\frac{1}{{{reta_a}}}x + {reta_c}"
        st.info(f"A equação da reta perpendicular é ${fracao}$ e está representada em azul. A reta original é $y = {reta_a}x + {reta_c}$ e está representada em vermelho.")
        
        # Definindo os limites dos eixos
        ax.set_xlim(-10, 10)
        ax.set_ylim(-10, 10)
        
        # Definindo os valores de x para cobrir todo o intervalo do gráfico
        x_values = np.linspace(-10, 10, 400)
        y_values_perpendicular = -1/reta_a * x_values + reta_c
        y_values = reta_a * x_values + reta_c
        
        # Plotando as retas
        ax.plot(x_values, y_values, 'r-', linewidth = 1)
        ax.plot(x_values, y_values_perpendicular, 'b-', linewidth = 1)    
        
    
    # Exibindo a grade
    ax.grid(True)

    # Exibindo o gráfico no Streamlit
    st.pyplot(fig)              

  
def retas():
    """Função para exibir a interface da funcionalidade de retas.
    """
    
    st.subheader("Retas")
    st.write("Aqui você pode calcular: a distância de um ponto a uma reta, verificar se uma é reta paralela e equação da reta perpendicular.")
    opcao = st.radio("Selecione uma opção:", ["Distância de um ponto a uma reta", "Verificar se uma reta é paralela", "Equação da reta perpendicular"])
    
    if opcao == "Distância de um ponto a uma reta":
        
        st.info("1. Para calcular a distância de um ponto a uma reta, você precisa da equação da reta e das coordenadas do ponto.")
        st.info("2. Aqui, consideramos a equação da reta na forma ($ax + by + c = 0$).")
        st.info("3. A distância de um ponto (x0, y0) a uma reta ax + by + c = 0 é dada pela fórmula: d = $\\frac{|ax + by + c|}{\\sqrt{a^2 + b^2}}$, onde d é a distância.")
        
        ponto_x = st.number_input("Digite a coordenada x do ponto:", value=0)
        ponto_y = st.number_input("Digite a coordenada y do ponto:", value=0)
        
        reta_a = st.number_input("Digite o coeficiente angular da reta (a):", value=0)
        reta_b = st.number_input("Digite o coeficiente linear da reta (b):", value=0)
        reta_c = st.number_input("Digite o termo independente da reta (c):", value=0)
        
        planoCartesianoReta(reta_a, reta_b, reta_c, ponto_x, ponto_y, distancia = True)
        
    elif opcao == "Verificar se uma reta é paralela":
        
        st.info("1. Para verificar se duas retas são paralelas, você precisa das equações das retas.")
        st.info("2. Duas retas são paralelas se seus coeficientes angulares forem iguais.")
        st.info("3. Se a1 = a2, então as retas são paralelas.")
        st.info("4. Se a1 != a2, então as retas não são paralelas.")
        st.info("5. Aqui, consideramos a equação da reta na forma (y = mx + c)")
        
        planoCartesianoReta(paralela = True)
    
    elif opcao == "Equação da reta perpendicular":
        
        st.info("1. Para calcular a equação da reta perpendicular, você só precisa da equação da reta.")
        st.info("2. A equação da reta perpendicular é dada por: $y = -\\frac{1}{m}x + c$, onde m é o coeficiente angular da reta original.")
        st.info("3. Aqui, consideramos a equação da reta na forma (y = mx + c)")
        st.info("4. Se a reta original for horizontal, a reta perpendicular será vertical e vice-versa.")
        
        
        planoCartesianoReta(perpendicular = True)
        
    
        
        
        
        
        
            
        # exibindo o gráfico
        
        
def planoCartesianoCircunferencia(equacao = None, centro_raio = None, ponto = None):
    
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
    
    if equacao:
        centro_x = st.number_input("Digite a coordenada x do centro da circunferência:", value=0)
        centro_y = st.number_input("Digite a coordenada y do centro da circunferência:", value=0)
        raio = st.number_input("Digite o raio da circunferência:", value=0)
        
        if raio < 0:
            st.error("O raio da circunferência não pode ser negativo.")
        else:
            st.info(f"A equação da circunferência é $(x - {centro_x})^2 + (y - {centro_y})^2 = {raio}^2$. O centro da circunferência é C({centro_x}, {centro_y}) e o raio é {raio}.")
            circle = plt.Circle((centro_x, centro_y), raio, color='b', fill=False)
            ax.add_artist(circle)
            
            # plotando o centro
            ax.plot(centro_x, centro_y, 'ro', markersize = 5)
            
            ax.annotate(f'C{centro_x, centro_y}', (centro_x, centro_y), textcoords="offset points", xytext=(-15,-15), ha='center', color='red', bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.2'))
            
            
            max_value = max(abs(centro_x), abs(centro_y), raio)
            
            # Definindo os limites dos eixos
            ax.set_xlim(-max_value-10, max_value+10)
            ax.set_ylim(-max_value-10, max_value+10)
            
            ax.set_aspect('equal')
        
        
    elif centro_raio:

        centro_x = st.number_input("Digite a coordenada x do centro da circunferência:", value=0)
        centro_y = st.number_input("Digite a coordenada y do centro da circunferência:", value=0)
        raio = st.number_input("Digite o raio da circunferência:", value=0)
        
        if raio < 0:
            st.error("O raio da circunferência não pode ser negativo.")
        else:
            st.info(f"O centro da circunferência é C({centro_x}, {centro_y}) e o raio é {raio}.")
            circle = plt.Circle((centro_x, centro_y), raio, color='b', fill=False)
            ax.add_artist(circle)
            
            # plotando o centro
            ax.plot(centro_x, centro_y, 'ro', markersize = 5)
            
            ax.annotate(f'C{centro_x, centro_y}', (centro_x, centro_y), textcoords="offset points", xytext=(-15,-15), ha='center', color='red', bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.2'))
            
            max_value = max(abs(centro_x), abs(centro_y), raio)
            
            # Definindo os limites dos eixos
            ax.set_xlim(-max_value-10, max_value+10)
            ax.set_ylim(-max_value-10, max_value+10)
            
            ax.set_aspect('equal')
        
    elif ponto:
        
        ponto_x = st.number_input("Digite a coordenada x do ponto:", value=0)
        ponto_y = st.number_input("Digite a coordenada y do ponto:", value=0)
        
        centro_x = st.number_input("Digite a coordenada x do centro da circunferência:", value=0)
        centro_y = st.number_input("Digite a coordenada y do centro da circunferência:", value=0)
        
        raio = st.number_input("Digite o raio da circunferência:", value=0)
        
        if raio < 0:
            st.error("O raio da circunferência não pode ser negativo.")
        else:
            distancia = ((ponto_x - centro_x)**2 + (ponto_y - centro_y)**2)**0.5
            
            if distancia > raio:
                st.info(f"O ponto ({ponto_x}, {ponto_y}) está fora da circunferência.")
            elif distancia < raio:
                st.info(f"O ponto ({ponto_x}, {ponto_y}) está dentro da circunferência.")
            else:
                st.info(f"O ponto ({ponto_x}, {ponto_y}) está na circunferência.")
            
            circle = plt.Circle((centro_x, centro_y), raio, color='b', fill=False)
            ax.add_artist(circle)
            
            # plotando o centro
            ax.plot(centro_x, centro_y, 'ro', markersize = 5)
            
            ax.annotate(f'C{centro_x, centro_y}', (centro_x, centro_y), textcoords="offset points", xytext=(-15,-15), ha='center', color='red', bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.2'))
            
            # plotando o ponto
            ax.plot(ponto_x, ponto_y, 'go', markersize = 5)
            
            ax.annotate(f'P{ponto_x, ponto_y}', (ponto_x, ponto_y), textcoords="offset points", xytext=(-15,-15), ha='center', color='green', bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.2'))
            
            max_value = max(abs(centro_x), abs(centro_y), raio, ponto_x, ponto_y)
            
            # Definindo os limites dos eixos
            ax.set_xlim(-max_value-10, max_value+10)
            ax.set_ylim(-max_value-10, max_value+10)
            
            ax.set_aspect('equal')
        
        
    
    # Exibindo a grade
    ax.grid(True)

    # Exibindo o gráfico no Streamlit
    st.pyplot(fig)
        
    


def circunferencias():
    """Função para exibir a interface da funcionalidade de circunferências.
    """
    
    st.subheader("Circunferências")
    st.write("Aqui, você pode calcular a equação da circunferência, o centro e o raio. Além disso, pode verificar se um ponto está dentro ou fora da circunferência.")
    opcao = st.radio("Selecione uma opção:", ["Equação da circunferência", "Plotar Centro e raio da circunferência", "Verificar se um ponto está dentro ou fora da circunferência"])
    
    if opcao == "Equação da circunferência":
        st.info("1. A equação da circunferência é dada por: $(x - h)^2 + (y - k)^2 = r^2$, onde (h, k) é o centro e r é o raio.")
        st.info("2. Se a circunferência não está no centro, a equação é dada por: $x^2 + y^2 + ax + by + c = 0$")
        st.info("3. Se a circunferência está no centro, a equação é dada por: $x^2 + y^2 = r^2$")
        
        planoCartesianoCircunferencia(equacao = True)
        
    elif opcao == "Plotar Centro e raio da circunferência":
        st.info("1. Para calcular o centro e o raio da circunferência, você precisa da equação da circunferência.")
        st.info("2. A equação da circunferência é dada por: $(x - h)^2 + (y - k)^2 = r^2$, onde (h, k) é o centro e r é o raio.")
        st.info("3. Se a circunferência não está no centro, a equação é dada por: $x^2 + y^2 + ax + by + c = 0$")
        st.info("4. Se a circunferência está no centro, a equação é dada por: $x^2 + y^2 = r^2$")
        
        planoCartesianoCircunferencia(centro_raio = True)
    
    elif opcao == "Verificar se um ponto está dentro ou fora da circunferência":
        st.info("1. Para verificar se um ponto está dentro ou fora da circunferência, você precisa das coordenadas do ponto e da equação da circunferência.")
        st.info("2. A equação da circunferência é dada por: $(x - h)^2 + (y - k)^2 = r^2$, onde (h, k) é o centro e r é o raio.")
        st.info("3. Se o ponto está dentro da circunferência, a distância do ponto ao centro é menor que o raio.")
        st.info("4. Se o ponto está fora da circunferência, a distância do ponto ao centro é maior que o raio.")
        st.info("5. Se o ponto está na circunferência, a distância do ponto ao centro é igual ao raio.")
        
        planoCartesianoCircunferencia(ponto = True)
    