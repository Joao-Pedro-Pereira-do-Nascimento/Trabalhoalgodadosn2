import networkx as ntx  # Biblioteca para trabalhar com o grafo
import matplotlib.pyplot as plt  # Biblioteca para ver o gráfico

grafo = ntx.Graph()  # Cria um grafo vazio

# Lista de nós a serem adicionados ao grafo
nos = ['A', 'B', 'C', 'D', 'E']
grafo.add_nodes_from(nos)  # Adiciona os nós ao grafo

# Lista de arestas com pesos para adicionar ao grafo
arestas = [
    # Aresta entre 'X' e 'Y' com peso Z
    ('A', 'B', 4),
    ('A', 'C', 2),
    ('B', 'C', 5),
    ('B', 'D', 10),
    ('C', 'D', 3),
    ('C', 'E', 8),
    ('D', 'E', 7)
]

grafo.add_weighted_edges_from(arestas)  # Adiciona as arestas com pesos ao grafo

# Nós origem e destino para encontrar o menor caminho
origem = 'A'
destino = 'E'

# Encontra o menor caminho entre os nós 'origem' e 'destino' considerando os pesos das arestas
caminho_menor = ntx.shortest_path(grafo, source=origem, target=destino, weight='weight')
# Calcula o comprimento do menor caminho
comprimento_caminho_menor = ntx.shortest_path_length(grafo, source=origem, target=destino, weight='weight')

# Imprime o menor caminho e o comprimento do caminho
print(f"Menor caminho de {origem} a {destino}: {caminho_menor}")
print(f"Comprimento do menor caminho: {comprimento_caminho_menor}")

# Desenha o grafo
posicoes = ntx.spring_layout(grafo)  # Calcula a posição dos nós usando o layout spring
plt.figure(figsize=(10, 8))  # Define o tamanho da figura para a visualização
ntx.draw(grafo, posicoes, with_labels=True, node_color='lightblue', node_size=2000, font_size=15, font_weight='bold', edge_color='gray')
# Mostra peso das arestas no grafo
etiquetas_aresta = ntx.get_edge_attributes(grafo, 'weight')
ntx.draw_networkx_edge_labels(grafo, posicoes, edge_labels=etiquetas_aresta)

# Só pra destacar o menor caminho no grafo
arestas_caminho = list(zip(caminho_menor, caminho_menor[1:]))  # Cria uma lista de arestas do menor caminho
ntx.draw_networkx_edges(grafo, posicoes, edgelist=arestas_caminho, edge_color='red', width=2.5)  # Desenha as arestas do menor caminho em vermelho

plt.title(f'Grafo Ponderado com Menor Caminho de {origem} a {destino}')
plt.show()  # Exibe o gráfico

