# Marco 2 — Representação Computacional

## Problema

Dominoes 2

## 1. Representação escolhida

Para representar o grafo será utilizada uma **lista de adjacência**, baseada nas implementações `Bag` e `Graph` disponibilizadas como referência na disciplina.

Cada vértice representa um dominó e possui uma estrutura `Bag` associada, responsável por armazenar os dominós que podem ser derrubados diretamente por ele.

Por exemplo, considerando as relações:

```text
1 -> 2
2 -> 3
```

a representação será:

```text
1: [2]
2: [3]
3: []
```

Como o problema possui relações direcionadas, uma ligação de `1` para `2` significa que a queda do dominó 1 pode provocar a queda do dominó 2, mas não significa que o dominó 2 possa derrubar o dominó 1.

A lista de adjacência foi escolhida por permitir armazenar somente as relações existentes entre os dominós, evitando a necessidade de representar todas as possíveis combinações entre eles.

---

## 2. Estrutura utilizada

A implementação utiliza uma coleção do tipo `Bag` para armazenar os vértices adjacentes.

Na classe `Digraph`, é criada uma `Bag` para cada dominó:

```python
self.adj = [Bag() for _ in range(self.V + 1)]
```

Foi utilizada uma posição adicional porque os dominós do problema são numerados a partir de 1.

Assim, `adj[1]` armazena os dominós que podem ser derrubados pelo dominó 1, `adj[2]` armazena os dominós que podem ser derrubados pelo dominó 2 e assim sucessivamente.

---

## 3. Leitura da entrada

Para cada caso de teste são lidos os valores `N`, `M` e `L`.

* `N` representa a quantidade de dominós;
* `M` representa a quantidade de relações entre os dominós;
* `L` representa a quantidade de dominós derrubados manualmente.

A partir de `N`, é criado um grafo direcionado:

```python
grafo = Digraph(n)
```

Em seguida são lidas `M` relações no formato:

```text
x y
```

Cada relação indica que a queda do dominó `x` provoca a queda do dominó `y`.

Essa relação é adicionada ao grafo por meio do método:

```python
grafo.add_edge(x, y)
```

Por fim, são lidos os `L` dominós que foram derrubados manualmente e armazenados em uma lista para utilização posterior.

---

## 4. Construção do grafo

Inicialmente, a classe `Digraph` cria uma estrutura `Bag` vazia para cada vértice.

Para cada relação `x -> y` encontrada na entrada, o vértice `y` é adicionado somente à lista de adjacência de `x`:

```python
self.adj[v].add(w)
```

Por exemplo, para a entrada:

```text
1 2
2 3
```

são adicionadas as seguintes arestas:

```text
1 -> 2
2 -> 3
```

resultando na representação:

```text
1: [2]
2: [3]
3: []
```

A implementação original da classe `Graph` utilizada como referência representa grafos não direcionados, adicionando a aresta nos dois sentidos.

No problema Dominoes 2, porém, as relações são direcionadas. Por esse motivo, a implementação foi adaptada para adicionar a ligação somente no sentido informado pela entrada.

---

## 5. Medidas estruturais

Considerando a instância utilizada no Marco 1:

```text
N = 3
M = 2
```

o grafo possui:

* **Ordem do grafo:** 3 vértices;
* **Tamanho do grafo:** 2 arestas.

O tamanho do grafo é armazenado na variável `E`, que é incrementada sempre que uma nova aresta é adicionada.

### Graus de saída

O grau de saída representa a quantidade de arestas que saem de determinado vértice.

Como cada `Bag` armazena os vizinhos alcançados diretamente pelo vértice, o grau de saída pode ser obtido pelo tamanho da `Bag`:

```python
def out_degree(self, v):
    return self.adj[v].size()
```

Para o exemplo:

* vértice 1: grau de saída = 1;
* vértice 2: grau de saída = 1;
* vértice 3: grau de saída = 0.

### Graus de entrada

O grau de entrada representa a quantidade de arestas que chegam a determinado vértice.

Para armazenar essa informação foi criado o vetor:

```python
self.grau_entrada = [0] * (self.V + 1)
```

Sempre que uma aresta `v -> w` é adicionada, o grau de entrada de `w` é incrementado:

```python
self.grau_entrada[w] += 1
```

Para o exemplo:

* vértice 1: grau de entrada = 0;
* vértice 2: grau de entrada = 1;
* vértice 3: grau de entrada = 1.

---

## 6. Validação com a instância pequena

A instância utilizada para validação é:

```text
1
3 2 1
1 2
2 3
2
```

Nessa entrada:

* existe 1 caso de teste;
* existem 3 dominós;
* existem 2 relações entre dominós;
* existe 1 dominó derrubado manualmente.

As relações são:

```text
1 -> 2
2 -> 3
```

O grafo construído apresenta a seguinte lista de adjacência:

```text
1: [2]
2: [3]
3: []
```

O dominó inicialmente derrubado é:

```text
2
```

As medidas estruturais obtidas são:

```text
Ordem: 3
Tamanho: 2

Vértice 1 - grau de entrada: 0 - grau de saída: 1
Vértice 2 - grau de entrada: 1 - grau de saída: 1
Vértice 3 - grau de entrada: 1 - grau de saída: 0
```

A representação mostra corretamente que o dominó 1 pode derrubar o dominó 2 e que o dominó 2 pode derrubar o dominó 3.

Dessa forma, a estrutura computacional representa corretamente as relações direcionadas fornecidas pela entrada.

Neste marco ainda não é realizada a busca pelos dominós alcançáveis. A implementação dos algoritmos DFS e BFS será realizada nos marcos seguintes.

---

## 7. Implementação de referência e adaptações

Foram utilizadas como referência as implementações `Bag` e `Graph` disponibilizadas no repositório da disciplina.

A estrutura `Bag` é utilizada para armazenar a lista de adjacência de cada vértice.

A classe `Graph` original foi adaptada para uma classe denominada `Digraph`, pois o problema Dominoes 2 possui relações direcionadas.

Na implementação original, uma aresta entre `v` e `w` é adicionada nos dois sentidos:

```python
self.adj[v].add(w)
self.adj[w].add(v)
```

Na versão adaptada para este problema, somente o sentido informado pela entrada é armazenado:

```python
self.adj[v].add(w)
```

Também foi adicionado um vetor para armazenar o grau de entrada de cada vértice, permitindo apresentar as medidas estruturais solicitadas no Marco 2.

Essas adaptações mantêm a estrutura da implementação de referência, mas permitem que ela represente corretamente o comportamento dos dominós no problema escolhido.
