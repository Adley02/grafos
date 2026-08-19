# Marco 2 — Representação Computacional

## 1. Escolha da Representação
A escolha ideal para este problema é a **Lista de Adjacência**.

* **Justificativa:** O problema informa que podemos ter até $10.000$ peças de dominó ($N$). 
  * Se usássemos uma *Matriz de Adjacência* ($N \times N$), criaríamos uma grade de $10.000 \times 10.000$ ($100$ milhões de posições). Isso consumiria muita memória e a maior parte estaria vazia, pois o limite de conexões ($M$) também é $10.000$. O grafo é esparso.
  * Com a *Lista de Adjacência*, criamos apenas uma lista para cada peça, contendo **apenas** os vizinhos que ela derruba diretamente. Se $N = 10.000$ e $M = 10.000$, gastaremos pouquíssima memória e o processamento será muito mais rápido.

---

## 2. Leitura da Entrada
A leitura precisará ser eficiente, pois podem haver múltiplos casos de teste e milhares de linhas de dados por caso.

1. Lemos o número de casos de teste.
2. Para cada caso, lemos a primeira linha com $N$ (peças), $M$ (conexões) e $L$ (empurrões manuais).
3. Faremos um laço de repetição que roda $M$ vezes para ler os pares ($x$, $y$), que são as regras de quem derruba quem.
4. Faremos outro laço de repetição que roda $L$ vezes para ler os inteiros $z$, que são as peças derrubadas inicialmente.

---

## 3. Construção do Grafo
Utilizaremos um *Vetor de Listas* (ou listas de listas, dependendo da linguagem). Como as peças são numeradas de $1$ a $N$, criaremos nosso vetor com tamanho $N + 1$ para podermos usar o número da peça diretamente como índice (ignorando a posição $0$).

* **Lógica de construção:** Ao ler a linha indicando que $x$ derruba $y$ (ex: `1 2`), acessamos a lista do vértice $x$ e adicionamos o vértice $y$ lá dentro.
  * `grafo[x].adicionar(y)`

---

## 4. Medidas Estruturais Pertinentes (Unidade I)
Avaliando a estrutura desse grafo de dominós, algumas medidas clássicas nos dão informações importantes:

* **Grau de Saída (Out-degree):** O número de elementos na lista de adjacência de um dominó $X$. Representa **quantas peças o dominó $X$ derruba diretamente**. Uma peça com grau de saída alto é uma peça crítica.
* **Grau de Entrada (In-degree):** Quantas setas apontam *para* uma peça. 
  * *Nota:* Se uma peça tem Grau de Entrada $= 0$, significa que nenhuma peça no jogo cai em cima dela. A única forma de ela cair é se estiver na lista dos empurrões manuais ($L$).
* **Densidade:** Como $M$ (arestas) tem limite máximo igual a $N$ (vértices), o grafo é extremamente esparso. O número de conexões é ínfimo perto do máximo possível num grafo direcionado (que seria $N \times (N-1)$).

---

## 5. Validação da Representação (Instância Pequena)
Vamos simular como a memória se comporta com a instância de teste do Marco 1.

**Instância (Input):**
```text
3 2 1  (N=3, M=2, L=1)
1 2    (Regra: 1 derruba 2)
2 3    (Regra: 2 derruba 3)
2      (Ação: 2 é empurrado)
```

**Representação na Memória (O Mapa):**
Criamos um vetor `Grafo` com índices de $1$ a $3$.
* `Grafo[1] = [2]` *(A lista do dominó 1 contém o 2)*
* `Grafo[2] = [3]` *(A lista do dominó 2 contém o 3)*
* `Grafo[3] = []` *(A lista do 3 está vazia, ele não derruba ninguém)*

**Fila de Ações Iniciais:**
* `Manuais = [2]`

**Validação:**
Quando o algoritmo executar, ele olhará para o vetor `Manuais` e verá que precisa iniciar pelo $2$. Ao acessar `Grafo[2]`, descobre que precisa derrubar o $3$. No `Grafo[3]` não há vizinhos, encerrando a propagação por esse caminho. O vértice $1$ nunca é ativado. A estrutura armazenou corretamente a topologia do problema de forma enxuta.
