# Marco 2 — Representação Computacional

## Problema

Dominoes 2

## 1. Representação escolhida

Para representar o grafo será utilizada uma lista de adjacência.

Cada posição da lista representa um dominó e contém os dominós
que são derrubados diretamente por ele.

Por exemplo, se existirem as relações:

1 -> 2
2 -> 3

a lista de adjacência será:

1: [2]
2: [3]
3: []

Como o grafo é direcionado, uma ligação de 1 para 2 não significa
necessariamente que exista uma ligação de 2 para 1.

<img width="364" height="237" alt="image" src="https://github.com/user-attachments/assets/d1164e21-b6d4-4590-824e-e54be401875d" />


A lista de adjacência foi escolhida por permitir armazenar diretamente
as relações de queda entre os dominós sem precisar representar todas
as possíveis combinações entre eles.


## 2. Leitura da entrada

Para cada caso de teste são lidos os valores N, M e L.

- N representa a quantidade de dominós;
- M representa a quantidade de relações entre dominós;
- L representa a quantidade de dominós derrubados manualmente.

Em seguida são lidas M relações no formato:

x y

Cada relação indica que a queda do dominó x provoca a queda do
dominó y.

Por fim, são lidos os L dominós que foram inicialmente derrubados
manualmente.


## 3. Construção do grafo

Inicialmente é criada uma lista vazia para cada dominó.

Para cada relação x -> y encontrada na entrada, o vértice y é
adicionado à lista de adjacência do vértice x.

Exemplo:

Entrada das relações:

1 2
2 3

Representação:

1: [2]
2: [3]
3: []


## 4. Medidas estruturais

Considerando a instância utilizada no Marco 1:

N = 3
M = 2

O grafo possui:

- Ordem do grafo: 3 vértices;
- Tamanho do grafo: 2 arestas.

Graus de saída:

- vértice 1: 1
- vértice 2: 1
- vértice 3: 0

Graus de entrada:

- vértice 1: 0
- vértice 2: 1
- vértice 3: 1


## 5. Validação com a instância pequena

Instância utilizada:

1
3 2 1
1 2
2 3
2

A lista de adjacência construída é:

1: [2]
2: [3]
3: []

O dominó inicialmente derrubado é:

2

A representação mostra corretamente que o dominó 2 possui uma
aresta direcionada para o dominó 3.

Assim, a estrutura computacional representa corretamente as relações
definidas na entrada.

Neste marco ainda não é executado o algoritmo de busca. A aplicação
de DFS e BFS será realizada nos marcos seguintes.
