# Algoritmos Elementares em Grafos

## 1. Introdução aos Grafos
![Exemplo de Grafo](https://upload.wikimedia.org/wikipedia/commons/c/c2/Aresta.png)

Grafos são estruturas matemáticas usadas para modelar relações entre objetos. Eles são compostos por dois elementos principais:

- **Vértices (ou nós)**: Representam os objetos ou entidades.
- **Arestas (ou arcos)**: Representam as conexões ou relações entre os vértices.

Grafos podem ser **direcionados** ou **não direcionados**:
- **Grafos direcionados**: As arestas possuem uma direção, indicando o caminho de um vértice para outro.
- **Grafos não direcionados**: As arestas não têm direção, e a conexão entre os vértices é bidirecional.

Além disso, grafos podem ser ponderados, onde cada aresta tem um peso associado, representando um custo, distância, ou qualquer outra métrica.
![Exemplo Grafos Formasfa]()

### 1.1 Aplicações de Grafos

Grafos são utilizados em uma ampla variedade de campos e aplicações, incluindo:
- **Redes de Computadores**: Para modelar a topologia da rede.
- **Sistemas de Navegação e GPS**: Para calcular rotas.
- **Redes Sociais**: Para representar conexões entre usuários.
- **Bioinformática**: Para modelar redes de interação entre proteínas.

![Exemplo Grafos Formasfa](https://www.infityworks.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fuw4iru0v%2Fproduction%2F464300b74929304a35d9b9c77de22cf31ece57c9-800x800.png&w=1080&q=85)

### 1.2 Algoritmos em Grafos

Os algoritmos de grafos são fundamentais para resolver problemas como:
- **Busca em Profundidade (DFS)**: Explora o grafo profundamente antes de retroceder.
- **Busca em Largura (BFS)**: Explora o grafo em níveis, visitando todos os vértices a uma determinada distância antes de avançar.
- **Detecção de Ciclos**: Verifica a presença de ciclos em um grafo.
- **Caminho Mínimo**: Encontra o menor caminho entre dois vértices em um grafo ponderado.

## 2. Algoritmo de Dijkstra

### 2.1 Visão Geral

O **Algoritmo de Dijkstra** é um algoritmo para encontrar o caminho mais curto entre dois vértices em um grafo ponderado, com a condição de que todas as arestas tenham pesos não negativos. Ele foi desenvolvido por Edsger Dijkstra em 1956 e é amplamente utilizado em sistemas de roteamento e navegação.

![Exemplo Dijkstra](https://user-images.githubusercontent.com/3193712/44612988-db180780-a7e3-11e8-82c9-b1ae318740c6.gif)


### 2.2 Funcionamento

O algoritmo funciona da seguinte maneira:

1. **Inicialização**:
   - Atribui-se a distância 0 ao vértice de origem e `infinito` para todos os outros vértices.
   - Cria-se um conjunto de vértices não visitados, que inicialmente inclui todos os vértices.

2. **Seleção do Vértice de Menor Distância**:
   - A cada iteração, escolhe-se o vértice não visitado com a menor distância conhecida (chamado de `vértice atual`).

3. **Atualização das Distâncias**:
   - Para cada vizinho do vértice atual, calcula-se a distância total desde a origem até esse vizinho através do vértice atual.
   - Se essa nova distância for menor do que a distância conhecida anteriormente, a distância é atualizada.

4. **Marcação como Visitado**:
   - Após processar todos os vizinhos, o vértice atual é marcado como visitado e removido do conjunto de vértices não visitados.

5. **Repetição**:
   - O processo repete-se até que todos os vértices tenham sido visitados ou que o menor caminho até o vértice de destino tenha sido determinado.

### 2.3 Complexidade

- **Tempo**: O tempo de execução do algoritmo de Dijkstra depende da implementação da estrutura de dados utilizada para a fila de prioridade. Com um heap binário, a complexidade é `O((V + E) log V)`, onde `V` é o número de vértices e `E` é o número de arestas.
- **Espaço**: O espaço requerido é `O(V)` para armazenar as distâncias e os predecessores.

### 2.4 Exemplo de Código em Python

Aqui está uma implementação básica do Algoritmo de Dijkstra usando Python:

```python
import heapq

def dijkstra(graph, start):
    # Inicializa as distâncias com infinito e a distância da origem como 0
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    
    # Usa uma fila de prioridade para gerenciar os vértices a serem explorados
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        # Se a distância atual é maior que a distância registrada, continue
        if current_distance > distances[current_vertex]:
            continue
        
        # Explora os vizinhos do vértice atual
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            # Se uma menor distância é encontrada, atualize a distância
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances
