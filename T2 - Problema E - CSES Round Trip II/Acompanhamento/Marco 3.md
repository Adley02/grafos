# Marco 3 — Estratégia algorítmica

## 1. Propriedade estrutural central

A propriedade estrutural central do problema **CSES Round Trip II** é a existência de um **ciclo em um grafo dirigido**.

Um ciclo dirigido ocorre quando é possível sair de um vértice, percorrer uma sequência de arestas respeitando suas direções e retornar ao vértice inicial.

O problema não exige encontrar o menor ciclo. Portanto, basta encontrar qualquer ciclo dirigido válido.

---

## 2. Estratégia escolhida

A estratégia escolhida é a **Busca em Profundidade (DFS) recursiva**.

A DFS é adequada para esse problema porque permite explorar um caminho do grafo em profundidade e identificar quando uma aresta retorna para um vértice que ainda faz parte do caminho atual da busca.

Para isso, são utilizadas três estruturas auxiliares principais:

- `marked[]`: indica se um vértice já foi visitado pela DFS;
- `onStack[]`: indica se o vértice ainda pertence ao caminho ativo da DFS;
- `edgeTo[]`: registra de qual vértice chegamos a cada vértice, permitindo posteriormente reconstruir o ciclo.

---

## 3. Critério para reconhecer um ciclo

Durante a DFS, considere uma aresta:

`v → w`

Podem ocorrer três situações principais:

1. Se `w` ainda não foi visitado, a DFS continua a partir de `w`.

2. Se `w` já foi visitado, mas não está mais no caminho atual da DFS, a busca continua normalmente.

3. Se `w` já foi visitado e:

`onStack[w] = true`

então o vértice `w` ainda pertence ao caminho atual da DFS.

Nesse caso, a aresta `v → w` retorna para um vértice ativo da busca, caracterizando uma **aresta de retorno** e indicando a existência de um ciclo dirigido.

---

## 4. Como obter a resposta

Encontrar um ciclo não é suficiente, pois o problema exige informar as cidades que pertencem ao ciclo.

Para isso, é utilizado o vetor:

`edgeTo[]`

Esse vetor registra o vértice anterior no caminho da DFS.

Quando uma aresta de retorno é encontrada, o `edgeTo[]` permite percorrer os vértices anteriores e reconstruir o ciclo.

---

## 5. Implementações de referência do algs4

As principais implementações de referência selecionadas são:

### `Digraph.java`

Será utilizada como referência para representar o grafo dirigido.

Cada cidade corresponde a um vértice e cada voo corresponde a uma aresta direcionada:

`a → b`

O grafo é armazenado por meio de listas de adjacência.

### `DirectedCycle.java`

Será a principal referência algorítmica.

Essa classe utiliza uma **DFS recursiva para grafos dirigidos** e possui as estruturas:

- `marked[]`;
- `onStack[]`;
- `edgeTo[]`.

A DFS utilizada não é importada de outra classe. O próprio `DirectedCycle.java` implementa seu método `dfs()`.

### Dependências utilizadas

A classe `Stack.java` é utilizada para armazenar os vértices pertencentes ao ciclo encontrado.

A classe `Bag.java` é utilizada internamente pela representação das listas de adjacência do `Digraph`.

Assim, as principais referências do trabalho são:

- `Digraph.java`;
- `DirectedCycle.java`.

`Stack.java` e `Bag.java` são estruturas auxiliares utilizadas pelas implementações.

---

## 6. Adaptações previstas

Nesta etapa ainda não será realizada a implementação.

Para a solução final, estão previstas as seguintes adaptações:

- leitura da quantidade de cidades e voos no formato utilizado pelo CSES;
- leitura das arestas dirigidas;
- adequação da numeração dos vértices;
- utilização da lógica de detecção de ciclos do `DirectedCycle`;
- reconstrução do ciclo encontrado;
- impressão da sequência de cidades pertencentes ao ciclo;
- impressão de `IMPOSSIBLE` caso nenhum ciclo seja encontrado.

O CSES utiliza cidades numeradas de `1` até `n`, enquanto as implementações do `algs4` normalmente utilizam vértices de `0` até `V - 1`. Essa diferença deverá ser considerada posteriormente na implementação.

---

## 7. Instância utilizada no rastreamento

Para realizar o rastreamento manual foi considerado o seguinte grafo dirigido:

`V = 4`

`E = 5`

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

Existe no grafo o ciclo:

```text
0 → 2 → 1 → 0
```

---

## 8. Rastreamento da DFS

Inicialmente:

```text
marked  = [F, F, F, F]

onStack = [F, F, F, F]

edgeTo  = [-, -, -, -]
```

O rastreamento é apresentado a seguir:

| Passo | Ação | `marked` | `onStack` | `edgeTo` | Decisão |
|---:|---|---|---|---|---|
| 0 | Estado inicial | `[F,F,F,F]` | `[F,F,F,F]` | `[-,-,-,-]` | Iniciar DFS |
| 1 | Entra em `DFS(0)` | `[T,F,F,F]` | `[T,F,F,F]` | `[-,-,-,-]` | Explorar vizinhos de 0 |
| 2 | Analisa `0 → 2` | `[T,F,F,F]` | `[T,F,F,F]` | `edgeTo[2]=0` | 2 não visitado, executar `DFS(2)` |
| 3 | Entra em `DFS(2)` | `[T,F,T,F]` | `[T,F,T,F]` | `[-,-,0,-]` | Explorar vizinhos de 2 |
| 4 | Analisa `2 → 1` | `[T,F,T,F]` | `[T,F,T,F]` | `edgeTo[1]=2` | 1 não visitado, executar `DFS(1)` |
| 5 | Entra em `DFS(1)` | `[T,T,T,F]` | `[T,T,T,F]` | `[-,2,0,-]` | Explorar vizinhos de 1 |
| 6 | Analisa `1 → 0` | `[T,T,T,F]` | `[T,T,T,F]` | `[-,2,0,-]` | `onStack[0] = true`, ciclo encontrado |

Nesse momento, o caminho ativo da DFS é:

```text
0 → 2 → 1
```

A aresta:

```text
1 → 0
```

retorna para o vértice `0`, que ainda está ativo na DFS.

Como:

```text
onStack[0] = true
```

é identificado o ciclo:

```text
0 → 2 → 1 → 0
```

O vértice `3` não precisa ser explorado para que a existência do ciclo seja comprovada.

---

## 9. Reconstrução do ciclo

Durante a DFS foram registrados:

```text
edgeTo[2] = 0
edgeTo[1] = 2
```

Assim, quando é encontrada a aresta:

```text
1 → 0
```

é possível utilizar o `edgeTo[]` para reconstruir:

```text
0 → 2 → 1
```

A nova aresta fecha o ciclo:

```text
0 → 2 → 1 → 0
```

Dessa forma, o `edgeTo[]` permite obter a sequência de vértices exigida como resposta pelo problema.

---

## 10. Complexidade de tempo

A DFS visita cada vértice no máximo uma vez e percorre as arestas presentes nas listas de adjacência.

Assim, a complexidade de tempo é:

```text
O(V + E)
```

onde:

- `V` representa a quantidade de vértices;
- `E` representa a quantidade de arestas.

Essa complexidade ocorre porque cada vértice é visitado uma vez e cada aresta é analisada durante a execução da busca.

---

## 11. Complexidade de espaço

A memória deve ser analisada separando a representação do grafo da memória auxiliar utilizada pelo algoritmo.

### Representação do grafo

Como o grafo é representado por listas de adjacência, o espaço utilizado é:

```text
O(V + E)
```

### Memória auxiliar

As estruturas utilizadas pela DFS são:

```text
marked[]  → O(V)

onStack[] → O(V)

edgeTo[]  → O(V)
```

A pilha utilizada para armazenar o ciclo pode ocupar:

```text
O(V)
```

Além disso, como a DFS é recursiva, a pilha de chamadas pode chegar a:

```text
O(V)
```

no pior caso.

Portanto, a memória auxiliar é:

```text
O(V)
```

Considerando também a representação do grafo, a memória total utilizada é:

```text
O(V + E)
```

---

## 12. Conclusão

A estratégia escolhida utiliza uma DFS recursiva para identificar ciclos em um grafo dirigido.

A principal condição utilizada é a existência de uma aresta que leva a um vértice que ainda está ativo no caminho da busca:

```text
onStack[w] = true
```

Essa situação caracteriza uma aresta de retorno e comprova a existência de um ciclo dirigido.

O vetor `edgeTo[]` permite reconstruir os vértices pertencentes ao ciclo encontrado.

As principais implementações utilizadas como referência são `Digraph.java` para a representação do grafo e `DirectedCycle.java` para a estratégia de busca e detecção do ciclo.

A estratégia apresenta complexidade de tempo `O(V + E)`, memória auxiliar `O(V)` e memória total `O(V + E)` considerando também a representação do grafo.
