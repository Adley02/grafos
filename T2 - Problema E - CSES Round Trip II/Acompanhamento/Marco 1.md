# Marco 1 — Problema e conhecimento prévio

## 1. Problema escolhido

O problema atribuído ao grupo é o **Problema E — CSES Round Trip II**.

O problema apresenta um conjunto de cidades conectadas por voos de sentido único. O objetivo é encontrar uma rota que comece em uma cidade, passe por uma ou mais cidades distintas e retorne à cidade inicial.

Portanto, o problema consiste em identificar a existência de um **ciclo em um grafo dirigido**.

---

## 2. Entrada

A primeira linha contém dois valores:

- `n`: número de cidades;
- `m`: número de voos.

Em seguida, são fornecidas `m` linhas contendo dois valores `a` e `b`, indicando a existência de um voo:

a → b

Os limites do problema são:

1 ≤ n ≤ 10^5

1 ≤ m ≤ 2·10^5

---

## 3. Saída

Caso exista uma viagem de ida e volta, deve ser informado:

- o número de cidades presentes na rota;
- a sequência de cidades que forma o ciclo.

Qualquer ciclo válido pode ser apresentado.

Caso nenhum ciclo exista, deve ser impressa a mensagem:

IMPOSSIBLE

---

## 4. Modelagem do grafo

Cada cidade é representada por um **vértice**.

Cada voo de uma cidade `a` para uma cidade `b` é representado por uma **aresta direcionada**:

a → b

O grafo é, portanto:

- dirigido;
- não ponderado;
- possivelmente desconexo.

A direção das arestas é importante, pois um voo `a → b` não significa necessariamente que exista também um voo `b → a`.

---

## 5. Resultado de aprendizagem

O principal conhecimento utilizado no problema é a aplicação da **Busca em Profundidade (DFS)** em grafos dirigidos.

A DFS será utilizada para percorrer os vértices e identificar se durante a exploração ocorre um retorno para um vértice que ainda pertence ao caminho atual da busca.

Essa situação caracteriza a existência de um ciclo dirigido.

Não é necessário encontrar o menor ciclo. Qualquer ciclo válido satisfaz o problema.

---

## 6. Instância pequena

Foi utilizada a seguinte instância:

V = 4
E = 5

Arestas:

0 → 2
2 → 1
1 → 0
1 → 3
2 → 3

Lista de adjacência:

0: [2]
1: [0, 3]
2: [1, 3]
3: []

O grafo possui o ciclo:

0 → 2 → 1 → 0

---

## 7. Rastreamento inicial

A DFS pode iniciar no vértice `0`.

A busca segue:

0 → 2 → 1

Ao chegar ao vértice `1`, existe a aresta:

1 → 0

O vértice `0` pertence ao caminho que está sendo explorado naquele momento.

Dessa forma, é possível identificar o ciclo:

0 → 2 → 1 → 0

O vértice `3` não precisa participar do ciclo.

---

## 8. Justificativa da utilização da DFS

A DFS é adequada porque o problema não exige encontrar o menor caminho ou o menor ciclo.

É necessário apenas encontrar qualquer ciclo dirigido válido.

A busca em profundidade permite acompanhar o caminho atualmente explorado e identificar quando uma aresta retorna para um vértice pertencente a esse caminho.

Essa propriedade será aprofundada nos próximos marcos por meio das estruturas auxiliares da DFS.
