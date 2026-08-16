# Problema dos Dominós (Dominoes 2)

O problema apresenta um conjunto de dominós em que a queda de um dominó pode provocar a queda de outro. Além disso, existem dominós que são derrubados de maneira manual, iniciando reações em cadeia.

## Objetivo
Determinar a quantidade total de dominós que caíram, somando os que foram derrubados manualmente com aqueles que caíram em consequência das reações em cadeia (efeito dominó).

---

## Modelagem do Grafo
* **Vértices:** As peças de dominó (numeradas de 1 a $N$).
* **Arestas:** A relação de causa e efeito na queda entre os dominós ($x \to y$).
* **Tipo do Grafo:** Grafo direcionado (dígrafo) e não-ponderado. É direcionado porque o fato de a queda de $x$ derrubar $y$ não garante que a queda de $y$ derrube $x$.

---

## Especificação da Entrada
A primeira linha da entrada contém um inteiro que representa a **quantidade de casos de teste**. Para cada caso de teste, os dados são estruturados da seguinte forma:

### 1. Parâmetros Iniciais
Uma linha contendo três números inteiros: **$N$**, **$M$** e **$L$**.
* **`N`**: O número total de peças de dominó.
* **`M`**: O número de conexões (relações de causa e efeito) entre as peças.
* **`L`**: O número de dominós que foram derrubados manualmente.

### 2. Conexões (Causa e Efeito)
As próximas **$M$** linhas contêm **2 valores inteiros** cada ($x$ e $y$), representando as conexões feitas entre as peças (isto é, a queda de $x$ provoca a queda de $y$).

### 3. Ações Manuais
Por fim, as **$L$** linhas seguintes contêm **1 inteiro** cada, indicando especificamente quais dominós foram derrubados com a mão.

---

## Especificação da Saída
Para cada caso de teste, deve ser apresentada em uma única linha a **quantidade total de dominós que caíram**.

---

## Restrições e Regras Importantes
* O número de peças, conexões e ações manuais ($N$, $M$ e $L$) pode ser de **até 10.000**.
* Os dominós são indexados de $1$ a $N$.

---

## Exemplo de Entrada e Saída

### Exemplo de Entrada
```text
1
3 2 1
1 2
2 3
2
```

### Resultado Esperado (Saída)
```text
2
```

---

## Hipótese Inicial de Solução
* Estamos utilizando um grafo direcionado porque a propagação da queda segue um fluxo unidirecional (efeito cascata).
