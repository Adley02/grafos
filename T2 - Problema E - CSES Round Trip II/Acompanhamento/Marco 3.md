# Marco 3 — Estratégia algorítmica

## 1. Propriedade estrutural central

A propriedade estrutural central do problema **CSES Round Trip II** é a existência de um **ciclo em um grafo dirigido**.

Cada cidade é representada por um vértice e cada voo é representado por uma aresta direcionada.

Um ciclo dirigido ocorre quando é possível sair de uma cidade, percorrer uma sequência de voos respeitando suas direções e retornar à cidade inicial.

O problema não exige encontrar o menor ciclo existente. Portanto, qualquer ciclo dirigido válido pode ser apresentado como resposta.

---

## 2. Estratégia algorítmica escolhida

A estratégia escolhida é a **Busca em Profundidade (DFS) recursiva**.

A DFS é adequada porque permite explorar um caminho do grafo em profundidade e identificar quando uma aresta retorna para um vértice que ainda pertence ao caminho atualmente explorado.

Para realizar esse controle são utilizadas principalmente três estruturas:

- `marked[]`: registra se um vértice já foi visitado;
- `on_stack[]`: registra se um vértice ainda pertence ao caminho ativo da DFS;
- `edge_to[]`: registra o vértice anterior utilizado para alcançar cada vértice.

Essas estruturas são utilizadas pela implementação de referência `directed_cycle.py` disponibilizada na biblioteca `algs4-py`.

---

## 3. Critério para reconhecer um ciclo

Durante a execução da DFS, considere uma aresta dirigida:

```text
v → w
```

Podem ocorrer três situações principais.

### Caso 1 — O vértice ainda não foi visitado

Se:

```text
marked[w] = False
```

o algoritmo registra:

```text
edge_to[w] = v
```

e continua a DFS a partir de `w`.

### Caso 2 — O vértice já foi visitado e não está mais no caminho ativo

Se:

```text
marked[w] = True
```

mas:

```text
on_stack[w] = False
```

o vértice já foi processado anteriormente e essa aresta não caracteriza um ciclo no caminho atual.

### Caso 3 — O vértice está no caminho ativo

Se:

```text
on_stack[w] = True
```

o vértice `w` ainda pertence à sequência de chamadas ativas da DFS.

Assim, a aresta:

```text
v → w
```

retorna para um vértice do próprio caminho que está sendo percorrido.

Essa situação caracteriza uma **aresta de retorno** e comprova a existência de um ciclo dirigido.

---

## 4. Obtenção da resposta

O problema não exige apenas informar que existe um ciclo. Também é necessário apresentar a sequência de cidades que forma esse ciclo.

Para isso é utilizado:

```text
edge_to[]
```

Esse vetor registra de qual vértice a DFS chegou a cada novo vértice.

Quando uma aresta de retorno é encontrada, o algoritmo utiliza os valores armazenados em `edge_to[]` para voltar pelo caminho percorrido e reconstruir os vértices pertencentes ao ciclo.

O ciclo reconstruído pode então ser armazenado em uma lista e posteriormente apresentado como resposta.

---

## 5. Implementações de referência selecionadas

Para o desenvolvimento da solução foram selecionadas implementações da biblioteca Python disponibilizada na disciplina em:

```text
algs4-py/algs4
```

As principais referências são:

### `directed_cycle.py`

É a principal referência algorítmica para o problema.

Essa implementação utiliza uma DFS recursiva para detectar ciclos em grafos dirigidos.

As principais estruturas utilizadas são:

```text
_marked[]
on_stack[]
edge_to[]
cycle
```

A lógica de detecção ocorre quando uma aresta encontra um vértice que ainda possui:

```text
on_stack[w] = True
```

A própria classe implementa a DFS utilizada para percorrer o grafo.

Portanto, não é utilizada uma DFS importada de outra classe.

---

### `digraph.py`

É utilizada como referência para representar o grafo dirigido.

Cada vértice possui sua própria lista de adjacência.

Para uma aresta:

```text
v → w
```

o vértice `w` é armazenado na lista de adjacência de `v`.

Como o problema utiliza voos de sentido único, a aresta não é adicionada automaticamente no sentido contrário.

---

### `bag.py`

A estrutura `Bag` é utilizada pelo `digraph.py` para armazenar os vértices presentes nas listas de adjacência.

Ela não representa um algoritmo para detecção de ciclos, mas funciona como uma estrutura auxiliar para a representação do grafo.

Assim, as principais referências algorítmicas selecionadas são:

```text
directed_cycle.py
digraph.py
```

e:

```text
bag.py
```

é utilizada como estrutura auxiliar da representação.

---

## 6. Adaptações previstas

Nesta etapa as adaptações são apenas planejadas. A implementação será realizada no Marco 4.

A estratégia das implementações de referência será mantida, realizando apenas as adaptações necessárias para o problema **CSES Round Trip II**.

Entre as adaptações previstas estão:

- leitura da entrada no formato utilizado pelo CSES;
- leitura da quantidade de cidades `n` e da quantidade de voos `m`;
- criação das arestas direcionadas;
- adequação da numeração dos vértices;
- utilização da DFS de detecção de ciclos;
- utilização de `marked`, `on_stack` e `edge_to`;
- reconstrução de um ciclo encontrado;
- impressão da quantidade de cidades pertencentes ao ciclo;
- impressão da sequência das cidades;
- impressão de `IMPOSSIBLE` caso nenhum ciclo exista;
- adequação da profundidade de recursão para os limites do problema.

A implementação Python disponibilizada na disciplina será utilizada como base, preservando a estratégia da classe `DirectedCycle` e adaptando principalmente a entrada e a saída exigidas pelo CSES.

---

## 7. Instância utilizada no rastreamento

Para realizar o rastreamento manual foi considerado um grafo dirigido com:

```text
V = 4
E = 5
```

Arestas:

```text
0 → 2
2 → 1
1 → 0
1 → 3
2 → 3
```

Lista de adjacência:

```text
0: [2]
1: [0, 3]
2: [1, 3]
3: []
```

Existe nesse grafo o ciclo:

```text
0 → 2 → 1 → 0
```

---

## 8. Estado inicial das estruturas

Antes da execução da DFS:

```text
marked  = [F, F, F, F]

on_stack = [F, F, F, F]

edge_to = [-, -, -, -]
```

Onde:

- `F` representa `False`;
- `marked` indica os vértices já visitados;
- `on_stack` indica os vértices ainda ativos na DFS;
- `edge_to` registra de qual vértice a busca chegou ao próximo.

---

## 9. Rastreamento da DFS

| Passo | Ação | `marked` | `on_stack` | `edge_to` | Decisão |
|---:|---|---|---|---|---|
| 0 | Estado inicial | `[F,F,F,F]` | `[F,F,F,F]` | `[-,-,-,-]` | Iniciar a busca |
| 1 | Entra em `DFS(0)` | `[T,F,F,F]` | `[T,F,F,F]` | `[-,-,-,-]` | Explorar vizinhos de 0 |
| 2 | Analisa `0 → 2` | `[T,F,F,F]` | `[T,F,F,F]` | `edge_to[2]=0` | 2 não foi visitado |
| 3 | Entra em `DFS(2)` | `[T,F,T,F]` | `[T,F,T,F]` | `[-,-,0,-]` | Explorar vizinhos de 2 |
| 4 | Analisa `2 → 1` | `[T,F,T,F]` | `[T,F,T,F]` | `edge_to[1]=2` | 1 não foi visitado |
| 5 | Entra em `DFS(1)` | `[T,T,T,F]` | `[T,T,T,F]` | `[-,2,0,-]` | Explorar vizinhos de 1 |
| 6 | Analisa `1 → 0` | `[T,T,T,F]` | `[T,T,T,F]` | `[-,2,0,-]` | `on_stack[0] = True`: ciclo encontrado |

---

## 10. Identificação do ciclo

No momento em que a DFS está no vértice `1`, o caminho ativo é:

```text
0 → 2 → 1
```

Nesse momento são verdadeiras as condições:

```text
on_stack[0] = True
on_stack[2] = True
on_stack[1] = True
```

Ao analisar a aresta:

```text
1 → 0
```

o algoritmo verifica:

```text
on_stack[0] = True
```

Isso significa que o vértice `0` ainda pertence ao caminho atual da DFS.

Portanto, a aresta retorna para um vértice ativo e forma o ciclo:

```text
0 → 2 → 1 → 0
```

O vértice `3` não precisa ser explorado para que a existência do ciclo seja comprovada, pois o problema solicita apenas um ciclo válido.

---

## 11. Reconstrução do ciclo utilizando `edge_to`

Durante a DFS foram armazenados:

```text
edge_to[2] = 0
edge_to[1] = 2
```

Isso representa o caminho:

```text
0 → 2 → 1
```

Quando é encontrada a aresta:

```text
1 → 0
```

o algoritmo pode percorrer os valores de `edge_to` para reconstruir os vértices anteriores.

Temos:

```text
1 ← 2 ← 0
```

Reorganizando na ordem da viagem:

```text
0 → 2 → 1
```

A aresta encontrada fecha o ciclo:

```text
0 → 2 → 1 → 0
```

Assim, `edge_to[]` permite obter a sequência de cidades necessária para produzir a saída do problema.

---

## 12. Papel do `on_stack`

O vetor `on_stack[]` possui uma função diferente de `marked[]`.

O vetor:

```text
marked[]
```

responde:

```text
Este vértice já foi visitado alguma vez?
```

Enquanto:

```text
on_stack[]
```

responde:

```text
Este vértice ainda pertence ao caminho que está sendo explorado neste momento?
```

Um vértice pode possuir:

```text
marked[v] = True
```

e:

```text
on_stack[v] = False
```

Isso significa que ele já foi visitado, mas sua exploração já terminou.

Por outro lado, quando:

```text
on_stack[v] = True
```

o vértice ainda pertence à cadeia atual de chamadas da DFS.

Por isso, encontrar uma aresta para um vértice com `on_stack = True` permite reconhecer um ciclo dirigido.

---

## 13. Complexidade de tempo

A DFS visita cada vértice no máximo uma vez.

Além disso, durante a busca são percorridas as listas de adjacência, fazendo com que as arestas sejam analisadas.

Dessa forma:

```text
Tempo = O(V + E)
```

onde:

- `V` representa a quantidade de vértices;
- `E` representa a quantidade de arestas.

A complexidade é linear em relação ao tamanho da representação do grafo.

O fato de o algoritmo poder encerrar a busca após encontrar um ciclo pode reduzir o número de operações em alguns casos, porém a complexidade de pior caso continua sendo:

```text
O(V + E)
```

---

## 14. Complexidade de espaço

A análise do espaço utilizado pode ser dividida entre a representação do grafo e a memória auxiliar do algoritmo.

### Representação do grafo

A representação por listas de adjacência necessita armazenar os vértices e as arestas.

Assim:

```text
O(V + E)
```

### Memória auxiliar

As estruturas:

```text
marked[]
on_stack[]
edge_to[]
```

possuem tamanho proporcional ao número de vértices:

```text
O(V)
```

A lista utilizada para armazenar o ciclo encontrado pode possuir até:

```text
O(V)
```

elementos.

Como a DFS é recursiva, a pilha de chamadas também pode atingir:

```text
O(V)
```

no pior caso.

Portanto:

```text
Memória auxiliar = O(V)
```

Considerando também a representação do grafo:

```text
Memória total = O(V + E)
```

---

## 15. Conclusão

A estratégia escolhida para o problema **CSES Round Trip II** é a utilização de uma DFS recursiva para detectar ciclos em um grafo dirigido.

As implementações de referência selecionadas na biblioteca Python da disciplina são:

```text
directed_cycle.py
digraph.py
```

com:

```text
bag.py
```

como estrutura auxiliar utilizada na representação do grafo.

A detecção do ciclo ocorre quando uma aresta alcança um vértice que ainda possui:

```text
on_stack[w] = True
```

Essa situação caracteriza uma aresta de retorno para um vértice pertencente ao caminho ativo da DFS.

O vetor `edge_to[]` permite posteriormente reconstruir os vértices que formam o ciclo.

A estratégia apresenta:

```text
Complexidade de tempo: O(V + E)

Memória auxiliar: O(V)

Memória total: O(V + E)
```

No Marco 4, essa estratégia será implementada a partir das versões Python disponibilizadas no `algs4-py`, realizando apenas as adaptações necessárias para o formato de entrada e saída do problema CSES Round Trip II.
