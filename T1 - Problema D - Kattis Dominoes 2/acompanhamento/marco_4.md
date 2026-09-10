# Marco 4 — Aplicação básica de BFS e conclusão

## Aplicação manual da BFS

Para comparar a Busca em Largura (**Breadth-First Search — BFS**) com a DFS utilizada na solução, foi considerado o mesmo exemplo do Marco 3:

```text
1 → 2
2 → 3
2 → 4
```

Representação:

```text
    1
    ↓
    2
   / \
  ↓   ↓
  3   4
```

Consideramos novamente o vértice `1` como ponto inicial.

A BFS utiliza uma fila e visita os vértices por níveis.

---

## Execução manual

Inicialmente:

```text
Fila = [1]
```

O vértice `1` possui distância `0`.

### Processamento do vértice 1

Retiramos `1` da fila e encontramos seu vizinho `2`.

```text
Fila = [2]
```

O vértice `2` está no nível 1.

---

### Processamento do vértice 2

Retiramos `2` da fila.

Seus vizinhos são `3` e `4`.

Ambos são adicionados à fila:

```text
Fila = [3, 4]
```

Os vértices `3` e `4` estão no nível 2.

---

### Processamento do vértice 3

O vértice `3` é retirado da fila.

Como não possui novos vizinhos:

```text
Fila = [4]
```

---

### Processamento do vértice 4

O vértice `4` é retirado da fila.

Ele também não possui novos vizinhos:

```text
Fila = []
```

A busca termina.

---

## Níveis da BFS

Os níveis obtidos foram:

```text
Nível 0: 1
Nível 1: 2
Nível 2: 3, 4
```

Visualmente:

```text
      1           nível 0
      |
      2           nível 1
     / \
    3   4         nível 2
```

---

## Distâncias

A distância representa a quantidade mínima de arestas entre o vértice inicial e cada vértice.

| Vértice | Distância |
|---|---:|
| 1 | 0 |
| 2 | 1 |
| 3 | 2 |
| 4 | 2 |

Portanto:

```text
dist[1] = 0
dist[2] = 1
dist[3] = 2
dist[4] = 2
```

---

## Predecessores da BFS

Os predecessores encontrados foram:

| Vértice | Predecessor |
|---|---|
| 1 | - |
| 2 | 1 |
| 3 | 2 |
| 4 | 2 |

Assim:

```text
pred[1] = -
pred[2] = 1
pred[3] = 2
pred[4] = 2
```

---

## Comparação entre DFS e BFS

Tanto DFS quanto BFS conseguem identificar todos os dominós alcançáveis a partir de um dominó inicialmente derrubado.

A DFS busca aprofundar o máximo possível antes de retornar.

No exemplo:

```text
1 → 2 → 3
        ↑
        retorna para 2
        ↓
        4
```

Uma possível ordem da DFS é:

```text
1, 2, 3, 4
```

Já a BFS percorre o grafo por níveis:

```text
1
2
3, 4
```

A BFS possui a vantagem de calcular naturalmente as menores distâncias em quantidade de arestas.

Entretanto, o problema Dominoes 2 não solicita a distância entre os dominós. É necessário apenas determinar quais dominós são alcançáveis e contar quantos caem.

Por esse motivo, a DFS foi escolhida para a solução final.

---

## Escolha justificada

A solução final utiliza DFS.

A escolha foi feita porque:

1. o problema exige apenas alcançabilidade;
2. não é necessário calcular o menor caminho;
3. não é necessário armazenar níveis ou distâncias;
4. a implementação de DFS fornecida como referência pôde ser adaptada diretamente;
5. cada vértice precisa ser visitado apenas uma vez.

A BFS também seria uma solução válida para o problema, mas suas informações adicionais de nível e distância não são necessárias para a resposta solicitada.

---

## Representação utilizada

O grafo foi implementado como um dígrafo utilizando lista de adjacência.

A implementação de referência utilizava a estrutura `Bag`:

```python
self.adj = [Bag() for _ in range(self.V)]
```

Na solução final foi utilizada a lista nativa do Python:

```python
self.adj = [[] for _ in range(self.V)]
```

A inserção de uma aresta direcionada é realizada por:

```python
self.adj[v].append(w)
```

Essa adaptação mantém a representação por lista de adjacência e elimina a necessidade das classes auxiliares `Bag`, `Node` e `LinkIterator`.

---

## Integração da solução

A solução final foi organizada em três partes principais:

### Digraph

Responsável pela criação e armazenamento do grafo direcionado.

```python
class Digraph:
    def __init__(self, v):
        self.V = v
        self.E = 0
        self.adj = [[] for _ in range(self.V)]

    def add_edge(self, v, w):
        self.adj[v].append(w)
        self.E += 1
```

### DepthFirstSearch

Responsável por visitar os dominós alcançáveis.

```python
class DepthFirstSearch:
    def __init__(self, G):
        self.marked = [False for _ in range(G.V)]
        self.count = 0

    def dfs(self, G, v):
        self.marked[v] = True
        self.count += 1

        for w in G.adj[v]:
            if not self.marked[w]:
                self.dfs(G, w)
```

### Main

Responsável por:

- ler os casos de teste;
- criar o grafo;
- adicionar as relações entre os dominós;
- ler os dominós derrubados manualmente;
- executar a DFS;
- imprimir a quantidade total.

---

## Adaptações realizadas

As principais adaptações em relação às implementações de referência foram:

- substituição da estrutura `Bag` pela lista nativa do Python;
- utilização de `append()` para adicionar adjacências;
- remoção de métodos do `Digraph` que não eram necessários ao problema;
- adaptação da DFS para permitir vários vértices iniciais;
- manutenção de um único vetor `marked` durante cada caso de teste;
- conversão da numeração dos dominós de `1..n` para os índices `0..n-1` utilizados pelo Python;
- criação de uma função `main()` compatível com a entrada do Kattis;
- aumento do limite de recursão do Python para a DFS.

---

## Testes

### Teste 1

Entrada:

```text
1
3 2 1
1 2
2 3
2
```

Grafo:

```text
1 → 2 → 3
```

O dominó `2` é derrubado manualmente.

Caem:

```text
2 e 3
```

Saída esperada:

```text
2
```

Saída obtida:

```text
2
```

---

### Teste 2

Entrada:

```text
1
4 3 1
1 2
2 3
2 4
1
```

Grafo:

```text
    1
    ↓
    2
   / \
  ↓   ↓
  3   4
```

O dominó `1` é derrubado manualmente.

Todos os quatro dominós caem.

Saída esperada:

```text
4
```

Saída obtida:

```text
4
```

---

## Complexidade

Considere:

```text
V = número de vértices/dominós
E = número de arestas/relações
L = número de dominós derrubados manualmente
```

A construção das listas de adjacência possui custo:

```text
O(V)
```

A leitura e inserção das arestas possui custo:

```text
O(E)
```

A DFS visita cada vértice no máximo uma vez e percorre cada aresta no máximo uma vez:

```text
O(V + E)
```

O processamento dos `L` dominós inicialmente derrubados possui custo:

```text
O(L)
```

Portanto, considerando o algoritmo completo:

```text
O(V + E + L)
```

Como `L <= V`, a complexidade assintótica pode ser simplificada para:

```text
O(V + E)
```

A complexidade de memória também é:

```text
O(V + E)
```

devido à lista de adjacência, ao vetor `marked` e à pilha de chamadas da DFS.

---

## Submissão no Kattis

Problema:

**Dominoes 2**

Plataforma:

**Kattis**

Link:

https://open.kattis.com/problems/dominoes2

### Resultado

> Atualizar esta seção após a submissão final.

Quando a solução obtiver `Accepted`, adicionar a evidência em:

```text
evidencias/accepted.png
```

e alterar esta seção para:

```text
Resultado da submissão: Accepted
```

---

## Ensaio da apresentação

A apresentação foi estruturada para demonstrar, de forma resumida:

```text
Problema
↓
Modelagem
↓
Representação computacional
↓
DFS/BFS
↓
Validação
```

Durante o ensaio, a explicação foi organizada para respeitar o limite de cinco minutos definido para a apresentação.

O código completo não será lido linha por linha. Serão apresentados apenas os trechos necessários para justificar a lista de adjacência, a DFS e as adaptações realizadas.

---

## Conclusão

A modelagem do Dominoes 2 como um grafo direcionado permitiu representar naturalmente as relações de queda entre os dominós.

DFS e BFS são capazes de encontrar todos os vértices alcançáveis a partir dos dominós inicialmente derrubados.

A DFS foi escolhida para a implementação final porque o problema exige apenas determinar a alcançabilidade, sem necessidade de calcular menores distâncias ou níveis.

A solução utiliza lista de adjacência e apresenta complexidade assintótica de:

```text
O(V + E)
```

A implementação final foi adaptada a partir dos códigos de referência da disciplina e integrada ao formato de entrada e saída exigido pelo Kattis.
