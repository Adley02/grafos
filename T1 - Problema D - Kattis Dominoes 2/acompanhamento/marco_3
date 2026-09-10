# Marco 3 — Aplicação básica de DFS

## Problema

**Kattis — Dominoes 2**

Neste marco foi aplicada a Busca em Profundidade, ou **Depth-First Search (DFS)**, ao grafo direcionado utilizado para representar o problema Dominoes 2.

No problema, cada dominó é representado por um vértice e cada relação de queda é representada por uma aresta direcionada.

Por exemplo:

```text
1 → 2
2 → 3
2 → 4
```

O grafo correspondente é:

```text
    1
    ↓
    2
   / \
  ↓   ↓
  3   4
```

Consideramos que o dominó `1` foi derrubado manualmente.

---

## Execução manual da DFS

A DFS começa no vértice `1`.

Inicialmente, nenhum vértice foi visitado:

```text
marked = [False, False, False, False]
```

### Visita ao vértice 1

O vértice `1` é marcado como visitado.

```text
marked = [True, False, False, False]
```

A lista de adjacência do vértice `1` contém o vértice `2`.

Assim, a DFS continua no vértice `2`.

---

### Visita ao vértice 2

O vértice `2` é marcado como visitado.

```text
marked = [True, True, False, False]
```

O vértice `2` possui dois vértices adjacentes:

```text
2 → 3
2 → 4
```

A DFS aprofunda primeiro no vértice `3`.

---

### Visita ao vértice 3

O vértice `3` é marcado como visitado.

```text
marked = [True, True, True, False]
```

Como o vértice `3` não possui vizinhos ainda não visitados, a busca retorna ao vértice `2`.

---

### Visita ao vértice 4

Ao retornar ao vértice `2`, ainda existe o vértice `4` não visitado.

A DFS visita o vértice `4`.

```text
marked = [True, True, True, True]
```

Como o vértice `4` também não possui vizinhos, a busca termina.

A ordem de descoberta foi:

```text
1 → 2 → 3 → 4
```

É importante observar que essa ordem não significa que exista uma aresta entre `3` e `4`.

A busca visita `3`, retorna para `2` e posteriormente visita `4`.

---

## Árvore de busca

A árvore produzida pela DFS é:

```text
    1
    |
    2
   / \
  3   4
```

As arestas utilizadas para descobrir novos vértices foram:

```text
1 → 2
2 → 3
2 → 4
```

---

## Estados de visita

Durante a execução da DFS, o vetor `marked` apresenta os seguintes estados:

| Etapa | Estado de `marked` |
|---|---|
| Inicial | `[False, False, False, False]` |
| Visita 1 | `[True, False, False, False]` |
| Visita 2 | `[True, True, False, False]` |
| Visita 3 | `[True, True, True, False]` |
| Visita 4 | `[True, True, True, True]` |

O vetor de marcação impede que um mesmo vértice seja processado mais de uma vez.

---

## Tempos de descoberta e término

Para demonstrar o funcionamento da DFS, foi considerado um contador de tempo incrementado a cada descoberta e término de vértice.

| Vértice | Descoberta | Término |
|---|---:|---:|
| 1 | 1 | 8 |
| 2 | 2 | 7 |
| 3 | 3 | 4 |
| 4 | 5 | 6 |

A execução ocorre da seguinte forma:

```text
t=1  Descobre 1
t=2  Descobre 2
t=3  Descobre 3
t=4  Termina 3
t=5  Descobre 4
t=6  Termina 4
t=7  Termina 2
t=8  Termina 1
```

Os tempos foram utilizados nesta execução manual para demonstrar a estrutura da DFS. Eles não precisam ser armazenados pela solução final do Dominoes 2, pois o problema exige apenas a quantidade de dominós derrubados.

---

## Predecessores

O predecessor indica por qual vértice cada vértice foi descoberto.

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

O vértice `1` não possui predecessor porque foi o vértice inicial da busca.

---

## Alcançabilidade

Partindo do vértice `1`, todos os vértices do exemplo são alcançáveis:

```text
1 → 2
    ├→ 3
    └→ 4
```

Portanto, se o dominó `1` for derrubado, os quatro dominós cairão.

Resultado esperado:

```text
4
```

No problema Dominoes 2, essa propriedade de alcançabilidade representa diretamente a propagação da queda dos dominós.

---

## Aplicabilidade ao problema

A DFS é adequada ao Dominoes 2 porque o objetivo é determinar todos os dominós que podem ser alcançados a partir dos dominós inicialmente derrubados.

Quando um dominó é visitado:

```python
self.marked[v] = True
self.count += 1
```

ele é marcado como derrubado e contado.

Em seguida, seus vizinhos são percorridos:

```python
for w in G.adj[v]:
    if not self.marked[w]:
        self.dfs(G, w)
```

Assim, a DFS reproduz a propagação das quedas no grafo.

---

## Adaptação da implementação de referência

Foi utilizada como referência a implementação de `DepthFirstSearch` disponibilizada no material da disciplina.

A lógica principal da DFS foi mantida:

```python
self.marked[v] = True
self.count += 1

for w in G.adj[v]:
    if not self.marked[w]:
        self.dfs(G, w)
```

A principal adaptação foi realizada no construtor.

Na implementação de referência, a DFS é iniciada a partir de um único vértice no momento da criação do objeto.

No Dominoes 2, podem existir vários dominós derrubados manualmente. Por isso, o objeto da DFS é criado primeiro:

```python
search = DepthFirstSearch(G)
```

e a busca é chamada posteriormente para cada dominó inicial que ainda não tenha sido visitado:

```python
if not search.marked[z]:
    search.dfs(G, z)
```

Dessa maneira, todos os dominós utilizam o mesmo vetor `marked`, evitando que um dominó seja contado mais de uma vez.

---

## Conclusão do Marco 3

A execução manual demonstrou que a DFS consegue percorrer corretamente todos os dominós alcançáveis a partir de um dominó inicialmente derrubado.

O vetor `marked` evita visitas repetidas e a variável `count` registra a quantidade total de dominós alcançados.

A DFS mostrou-se aplicável ao problema porque a propagação da queda dos dominós pode ser tratada como uma busca pelos vértices alcançáveis de um grafo direcionado.
