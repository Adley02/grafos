# Marco 2 — Componentes conexas

## 1. Adaptação do problema

Para este marco, foi considerado um caso particular do problema e o grafo foi adaptado para um **grafo simples e não dirigido**, conforme solicitado.

Foi utilizado um grafo contendo:

V = 4
E = 5

As arestas são:

0 — 1
0 — 2
1 — 2
1 — 3
2 — 3

Nesta etapa, a direção dos voos do problema original é desconsiderada para permitir o estudo de componentes conexas e das propriedades métricas do grafo.

---

## 2. Lista de adjacência

A representação por lista de adjacência é:

0: [1, 2]
1: [0, 2, 3]
2: [0, 1, 3]
3: [1, 2]

Como o grafo é não dirigido, cada aresta aparece nas listas dos dois vértices envolvidos.

---

## 3. Componentes conexas

Todos os vértices podem ser alcançados uns a partir dos outros.

Portanto, existe apenas uma componente conexa:

C0 = {0, 1, 2, 3}

---

## 4. Distâncias

A matriz de menores distâncias é:

| Origem | 0 | 1 | 2 | 3 |
|---|---:|---:|---:|---:|
| 0 | 0 | 1 | 1 | 2 |
| 1 | 1 | 0 | 1 | 1 |
| 2 | 1 | 1 | 0 | 1 |
| 3 | 2 | 1 | 1 | 0 |

---

## 5. Excentricidades

A excentricidade corresponde à maior distância mínima de um vértice para os demais vértices da mesma componente.

Assim:

e(0) = 2

e(1) = 1

e(2) = 1

e(3) = 2

O raio é a menor excentricidade:

r = 1

O diâmetro é a maior excentricidade:

d = 2

Os vértices que apresentam excentricidade igual ao raio são `1` e `2`.

Portanto:

Centro = {1, 2}

---

## 6. Identificação da componente utilizando DFS

Foi utilizado um vetor denominado `componente[]`.

Inicialmente:

componente = [-1, -1, -1, -1]

O valor `-1` indica que o vértice ainda não foi visitado.

A DFS é iniciada no vértice `0`.

### Rastreamento

| Passo | Operação | Vetor componente |
|---|---|---|
| 0 | Estado inicial | `[-1,-1,-1,-1]` |
| 1 | Visita `0` | `[0,-1,-1,-1]` |
| 2 | `0 → 1` e visita `1` | `[0,0,-1,-1]` |
| 3 | `1 → 2` e visita `2` | `[0,0,0,-1]` |
| 4 | `2 → 3` e visita `3` | `[0,0,0,0]` |

A ordem de descoberta utilizada foi:

0 → 1 → 2 → 3

Ao término da DFS:

componente = [0, 0, 0, 0]

Portanto, todos os vértices pertencem à mesma componente conexa.

---

## 7. Complexidade de tempo

A DFS apresenta complexidade:

O(V + E)

Cada vértice é visitado uma única vez e todas as listas de adjacência são percorridas.

No grafo não dirigido, cada aresta aparece duas vezes nas listas de adjacência, mas esse fator constante não altera a complexidade assintótica.

Assim, o tempo permanece:

O(V + E)

---

## 8. Complexidade de espaço

O vetor `componente[]` ocupa:

O(V)

Como a DFS utilizada é recursiva, a pilha de chamadas pode possuir até `V` vértices no pior caso.

Portanto, a memória auxiliar é:

O(V)

Considerando também a representação do grafo por lista de adjacência, a memória total utilizada é:

O(V + E)

---

## 9. Custo das consultas de conectividade

Depois do processamento pela DFS, cada vértice possui armazenado o identificador de sua componente.

Para verificar se dois vértices `u` e `v` estão conectados, basta comparar:

componente[u] == componente[v]

Por exemplo:

componente[0] = 0
componente[3] = 0

Portanto, os vértices `0` e `3` estão conectados.

Como são necessários apenas dois acessos ao vetor e uma comparação, cada consulta possui custo:

O(1)

O pré-processamento necessário para construir o vetor de componentes custa:

O(V + E)

Para `Q` consultas, o custo total pode ser representado por:

O(V + E + Q)
