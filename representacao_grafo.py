import turtle  # 🐢 Biblioteca para desenho
import time    # ⏱️ Biblioteca para pausas

# Função para desenhar um nó
def draw_node(x, y, label, color):
    turtle.penup()  # ✋ Levanta a caneta para mover sem desenhar
    turtle.goto(x, y - 20)  # 📍 Move para a posição do nó
    turtle.pendown()  # 🖊️ Abaixa a caneta para começar a desenhar
    turtle.color(color)  # 🎨 Define a cor do nó
    turtle.begin_fill()  # 🟢 Começa a preencher a forma
    turtle.circle(20)  # 🔵 Desenha um círculo com raio 20
    turtle.end_fill()  # 🟡 Finaliza o preenchimento da forma
    turtle.penup()  # ✋ Levanta a caneta
    turtle.goto(x, y - 10)  # 📍 Move um pouco para baixo para escrever o rótulo
    turtle.pendown()  # 🖊️ Abaixa a caneta
    turtle.color("black")  # 🖤 Define a cor do texto
    turtle.write(label, align="center", font=("Arial", 12, "normal"))  # ✏️ Escreve o rótulo no nó

# Função para desenhar uma aresta
def draw_edge(x1, y1, x2, y2, label):
    turtle.penup()  # ✋ Levanta a caneta
    turtle.goto(x1, y1)  # 📍 Move para o ponto inicial da aresta
    turtle.pendown()  # 🖊️ Abaixa a caneta
    turtle.color("blue")  # 🔵 Define a cor da aresta
    turtle.goto(x2, y2)  # 📍 Desenha a linha até o ponto final
    mid_x = (x1 + x2) / 2  # 🧮 Calcula o ponto médio
    mid_y = (y1 + y2) / 2  # 🧮 Calcula o ponto médio
    turtle.penup()  # ✋ Levanta a caneta
    turtle.goto(mid_x, mid_y)  # 📍 Move para o ponto médio
    turtle.pendown()  # 🖊️ Abaixa a caneta
    turtle.color("black")  # 🖤 Define a cor do texto
    turtle.write(label, align="center", font=("Arial", 10, "normal"))  # ✏️ Escreve o rótulo da aresta

# Função para desenhar a legenda
def draw_legend():
    turtle.penup()  # ✋ Levanta a caneta
    turtle.goto(-200, -150)  # 📍 Move para a posição da legenda
    turtle.pendown()  # 🖊️ Abaixa a caneta
    turtle.color("black")  # 🖤 Define a cor do texto
    turtle.write("Legenda:", align="left", font=("Arial", 14, "bold"))  # ✏️ Escreve o título da legenda
    
    colors = ["red", "green", "yellow", "orange", "purple"]  # 🌈 Lista de cores dos nós
    labels = ["A", "B", "C", "D", "E"]  # 🏷️ Rótulos dos nós
    x_start = -150  # 📍 Posição inicial no eixo X para a legenda
    y_start = -170  # 📍 Posição inicial no eixo Y para a legenda

    # Desenha cada item da legenda
    for i, (color, label) in enumerate(zip(colors, labels)):
        turtle.penup()  # ✋ Levanta a caneta
        turtle.goto(x_start + (i * 80), y_start)  # 📍 Move para a posição do item da legenda
        turtle.pendown()  # 🖊️ Abaixa a caneta
        turtle.color(color)  # 🎨 Define a cor do item da legenda
        turtle.begin_fill()  # 🟢 Começa a preencher o item
        turtle.circle(10)  # 🔵 Desenha um círculo pequeno
        turtle.end_fill()  # 🟡 Finaliza o preenchimento
        turtle.penup()  # ✋ Levanta a caneta
        turtle.goto(x_start + (i * 80) + 20, y_start - 10)  # 📍 Move para o local do texto
        turtle.pendown()  # 🖊️ Abaixa a caneta
        turtle.color("black")  # 🖤 Define a cor do texto
        turtle.write(f"- Nó {label}", align="left", font=("Arial", 12, "normal"))  # ✏️ Escreve a descrição do item da legenda

# Função para exibir uma caixa de informação
def show_info_box():
    turtle.penup()  # ✋ Levanta a caneta
    turtle.goto(-200, -300)  # 📍 Move para a posição da caixa de informação
    turtle.pendown()  # 🖊️ Abaixa a caneta
    turtle.color("lightgrey")  # ⚪ Define a cor de fundo da caixa
    turtle.begin_fill()  # 🟢 Começa a preencher a caixa
    for _ in range(2):  # 🔁 Desenha um retângulo
        turtle.forward(400)  # → Desenha uma linha horizontal
        turtle.right(90)  # 🔄 Vira 90 graus
        turtle.forward(120)  # ↓ Desenha uma linha vertical
        turtle.right(90)  # 🔄 Vira 90 graus
    turtle.end_fill()  # 🟡 Finaliza o preenchimento

    turtle.penup()  # ✋ Levanta a caneta
    turtle.goto(-190, -290)  # 📍 Move para a posição do título da caixa
    turtle.pendown()  # 🖊️ Abaixa a caneta
    turtle.color("black")  # 🖤 Define a cor do texto
    turtle.write("Sobre o Grafo:", align="left", font=("Arial", 14, "bold"))  # ✏️ Escreve o título da caixa
    
    info_text = [  # 📝 Texto informativo
        "Um grafo é uma estrutura composta por vértices (nós)",
        "e arestas que conectam pares de vértices.",
        "",
        "Usos comuns:",
        "- Redes de comunicação",
        "- Sistemas de transporte",
        "- Bioinformática"
    ]
    
    turtle.penup()  # ✋ Levanta a caneta
    turtle.goto(-190, -310)  # 📍 Move para a posição do primeiro linha do texto
    turtle.pendown()  # 🖊️ Abaixa a caneta
    turtle.color("black")  # 🖤 Define a cor do texto
    
    # Desenha cada linha do texto informativo
    for line in info_text:
        turtle.write(line, align="left", font=("Arial", 12, "normal"))  # ✏️ Escreve a linha
        turtle.penup()  # ✋ Levanta a caneta       
        turtle.goto(turtle.xcor(), turtle.ycor() - 20)  # 📍 Move para baixo para a próxima linha
        turtle.pendown()  # 🖊️ Abaixa a caneta

# Configuração inicial
turtle.setup(width=800, height=600)  # 🌍 Define o tamanho da janela
turtle.speed(1)  # 🚶 Define a velocidade de desenho
turtle.hideturtle()  # 👻 Esconde a tartaruga para uma visualização limpa

# Coordenadas dos nós e suas cores
nodes = {
    "A": (-100, 100, "red"),
    "B": (100, 100, "green"),
    "C": (-100, -100, "yellow"),
    "D": (100, -100, "orange"),
    "E": (0, 0, "purple")
}

# Desenhar nós
for label, (x, y, color) in nodes.items():
    draw_node(x, y, label, color)  # 🖼️ Desenha o nó
    time.sleep(1)  # ⏱️ Pausa para visualização

# Desenhar arestas e rótulos
edges = [
    ("A", "B", "AB"),
    ("A", "C", "AC"),
    ("B", "D", "BD"),
    ("C", "D", "CD"),
    ("C", "E", "CE"),
    ("D", "E", "DE")
]

for edge in edges:
    x1, y1 = nodes[edge[0]][0], nodes[edge[0]][1]  # 📍 Coleta coordenadas do nó inicial
    x2, y2 = nodes[edge[1]][0], nodes[edge[1]][1]  # 📍 Coleta coordenadas do nó final
    draw_edge(x1, y1, x2, y2, edge[2])  # 🖼️ Desenha a aresta
    time.sleep(1)  # ⏱️ Pausa para visualização

# Desenhar a legenda
draw_legend()  # 🖼️ Desenha a legenda

# Exibir a caixa de informação
show_info_box()  # 🖼️ Exibe a caixa de informação

# Manter a janela aberta
turtle.done()  # 🎬 Finaliza o desenho e mantém a janela aberta
