import networkx as ntx
import matplotlib.pyplot as plt

# Cria o grafo para a fase de grupos
grafo_torneio = ntx.DiGraph()  # Grafo dirigido para representar a estrutura do torneio

times = ['Brasil', 'Argentina', 'Uruguai', 'Colômbia']  # Lista de times (nós) para adicionar ao grafo
grafo_torneio.add_nodes_from(times)  # Adiciona os times como nós ao grafo

# Lista de partidas na fase de grupos, com os resultados como atributos das arestas
partidas_fase_grupos = [
    ('Brasil', 'Argentina', {'resultado': 'Brasil vence'}),
    ('Brasil', 'Uruguai', {'resultado': 'Uruguai vence'}),
    ('Brasil', 'Colômbia', {'resultado': 'Brasil vence'}),
    ('Argentina', 'Uruguai', {'resultado': 'Empate'}),
    ('Argentina', 'Colômbia', {'resultado': 'Argentina vence'}),
    ('Uruguai', 'Colômbia', {'resultado': 'Uruguai vence'})
]

grafo_torneio.add_edges_from(partidas_fase_grupos)  # Partidass com resultados adicionadas ao grafo

# Transições para a fase de mata-mata
fase_mata_mata = [('Brasil', 'Oitavas de Final'),
                  ('Uruguai', 'Oitavas de Final')]

# Cria o grafo separado para a fase de mata-mata
grafo_fase_mata_mata = ntx.DiGraph()
grafo_fase_mata_mata.add_nodes_from(['Oitavas de Final', 'Quartas de Final', 'Semifinal', 'Final'])  # Estágios de mata-mata como nós
grafo_fase_mata_mata.add_edges_from([  # Transições entre os estágios de mata-mata
    ('Oitavas de Final', 'Quartas de Final'),
    ('Quartas de Final', 'Semifinal'),
    ('Semifinal', 'Final')
])

# Configurar o grafo da faswe de grupos
plt.figure(figsize=(12, 6))  # Tamanho da figura para a visualização
posicoes = ntx.circular_layout(grafo_torneio)  # Calcula a posição dos nós usando o layout circular
ntx.draw(grafo_torneio, posicoes, with_labels=True, node_color='lightblue', node_size=2000, font_size=15, font_weight='bold', edge_color='gray')
etiquetas_partidas = ntx.get_edge_attributes(grafo_torneio, 'resultado')
ntx.draw_networkx_edge_labels(grafo_torneio, posicoes, edge_labels=etiquetas_partidas)

# Título da fase de grupos
plt.title('Estrutura da Fase de Grupos da Copa do Mundo')
plt.show()

# Configurar o grafo da fase de mata-mata
plt.figure(figsize=(12, 6))
posicoes2 = ntx.circular_layout(grafo_fase_mata_mata)
ntx.draw(grafo_fase_mata_mata, posicoes2, with_labels=True, node_color='lightblue', node_size=8000, font_size=15, font_weight='bold', edge_color='gray')

# Etiquetas para fase de mata-mata
etiquetas_mata_mata = {
    ('Oitavas de Final', 'Quartas de Final'): 'Quartas de Final <- Oitavas de Final',
    ('Quartas de Final', 'Semifinal'): 'Semifinal <- Quartas',
    ('Semifinal', 'Final'): 'Final <- Semifinal'
}
ntx.draw_networkx_edge_labels(grafo_fase_mata_mata, posicoes2, edge_labels=etiquetas_mata_mata)

# Ti´tulo ao grafo da fase de mata-mata
plt.title('Estrutura da Fase de Mata-Mata da Copa do Mundo')
plt.show()

