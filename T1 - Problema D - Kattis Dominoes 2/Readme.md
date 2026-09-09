# Trabalho Prático 1 — Resolução de Problemas com Grafos

## Problema

O problema da nossa equipe foi o **Dominoes 2**, da plataforma Kattis.

O enunciado apresenta uma sequência de dominós e relações entre eles. Cada relação informa que, quando um determinado dominó cai, ele pode provocar a queda de outro.

Além disso, alguns dominós são derrubados manualmente.

O objetivo do problema é calcular quantos dominós cairão no total depois do primeiro dominó ser derrubado manualmente.

---

## Integrantes

Arthur Gomes de Aguiar = 1810460

Guilherme Adley        = 2020670


## Linguagem utilizada

A solução foi desenvolvida em Python 3

---

## Modelagem do problema

O problema foi modelado utilizando um **grafo direcionado(Digrafo)**.

Cada dominó representa um vértice do grafo.

Uma relação `x -> y` representa que, se o dominó `x` cair, ele provoca a queda do dominó `y`.

Por exemplo:

1 -> 2  
2 -> 3

representa:

1 -> 2 -> 3

Esse grafo precisa ser direcionado porque o fato de o dominó 1 derrubar o dominó 2 não significa necessariamente que o dominó 2 consiga derrubar o dominó 1.

---

## Vértices e arestas

Os **vértices** representam os dominós.

As **arestas** representam as relações de queda entre eles.

Exemplo:

1 -> 2

significa que o dominó 1 derruba o dominó 2.

---

## Representação computacional

O grafo foi representado utilizando uma **lista de adjacência**.

##Implementação de referência

Foram utilizadas como referência as implementações fornecidas no repositório da disciplina.

As principais referências utilizadas foram:

digraph.py
depth_first_search.py

A estrutura da classe Digraph foi utilizada como base para representar o grafo direcionado.

A estrutura da busca em profundidade também foi adaptada a partir do código de referência.

---

## Alteração do Bag para lista

Na implementação original do Digraph, a lista de adjacência utiliza a estrutura Bag.

O código original utiliza:

self.adj = [Bag() for _ in range(self.V)]

Na solução desenvolvida, essa estrutura foi substituída por listas nativas do Python:

self.adj = [[] for _ in range(self.V)]

Também foi utilizado:

self.adj[v].append(w)

para adicionar um vértice adjacente.

Essa alteração foi feita para simplificar a implementação e reduzir dependências externas, mantendo a mesma ideia de representação por lista de adjacência.

---

## Algoritmo utilizado

Foi utilizada a Busca em Profundidade, ou Depth First Search (DFS).

Quando um dominó é derrubado, a DFS visita esse vértice e continua percorrendo todos os dominós que podem ser derrubados a partir dele.

Cada vértice visitado é marcado para evitar que seja processado novamente.

---

## Complexidade de memória

Como foi utilizada uma lista de adjacência, a memória utilizada é proporcional ao número de vértices e arestas.

Assim, a complexidade de memória é:

O(V + E)

Teste de exemplo

---

## Teste de exemplo

Entrada:

1

3 2 1

1 2

2 3

2

Interpretação:

Existem 3 dominós.

As relações são:

1 -> 2

2 -> 3

O dominó 2 é derrubado manualmente.

Portanto, caem:

2 -> 3

Total de dominós derrubados:

2

Saída:

2

---

## Uso de Inteligência Artificial

Foi utilizada Inteligência Artificial como ferramenta de apoio durante o desenvolvimento do trabalho.

A ferramenta foi utilizada para auxiliar na compreensão do enunciado, na análise dos códigos de referência, na adaptação do Digraph, na escolha da representação por lista de adjacência e na compreensão da DFS.

O código foi analisado, testado e adaptado pelos integrantes do grupo.


