# Marco 1 — Formulação: Treehouses

**Disciplina:** Resolução de Problemas com Grafos  
**Problema:** [Treehouses — Kattis](https://open.kattis.com/problems/treehouses)  
**Classe:** Árvore Geradora Mínima (MST)  
**Enunciado:** [T3 — Ricardo Carubbi](https://github.com/carubbi/RPG/blob/main/mat-didatico/trabalhos/T3.md)

### 1.1 Resumo do problema

O problema **Treehouses** apresenta casas construídas em árvores que precisam ficar conectadas para permitir o deslocamento de pessoas entre elas. A conexão pode ser feita por cabos, que funcionam como ligações de passagem entre as casas — **não se trata de uma rede elétrica**.

Algumas casas já possuem acesso por terra e determinados pares de casas podem já estar conectados por cabos. Essas ligações existentes não exigem a instalação de novos cabos. O desafio consiste em determinar **o menor comprimento total de cabos novos** necessário para que todas as casas fiquem acessíveis por meio da rede de conexões.

### 1.2 Entrada, saída, objetivo e restrições

**Entrada:**

- `n`: número de casas nas árvores;
- `e`: quantidade de casas iniciais que já possuem acesso por terra (casas de `1` até `e`);
- `p`: quantidade de cabos já instalados entre pares de casas;
- `n` pares de coordenadas reais `(x, y)`, que indicam a posição de cada casa;
- `p` pares de identificadores de casas, que indicam os cabos já existentes.

**Saída:** um número real que representa o **comprimento mínimo total dos novos cabos** necessários para completar a conexão das casas.

**Objetivo:** minimizar a soma das distâncias dos novos cabos instalados, garantindo que todas as casas estejam conectadas à rede acessível.

**Condições importantes:**

1. As primeiras `e` casas já são acessíveis por terra e, portanto, pertencem à mesma rede inicial.
2. Cada cabo já instalado conecta as duas casas indicadas sem custo adicional de construção.
3. É possível considerar uma nova ligação direta entre qualquer par de casas, com comprimento calculado a partir de suas coordenadas.
4. A solução precisa conectar todas as casas, mas não precisa instalar cabos redundantes que apenas criariam ciclos.
5. O resultado deve respeitar a tolerância numérica estabelecida pelo Kattis (erro absoluto ou relativo menor que `0.001`).

### 1.3 Modelagem em grafo

O problema é representado por um **grafo ponderado e não direcionado**:

| Elemento | Representação no Treehouses |
|---|---|
| Vértices (`V`) | Casas nas árvores. |
| Arestas (`E`) | Possíveis ligações diretas entre pares de casas. |
| Peso de uma nova aresta | Comprimento do cabo, calculado pela distância euclidiana. |
| Direção | Não direcionado: a ligação pode ser percorrida nos dois sentidos. |
| Conexões existentes | Casas já ligadas por terra ou por cabos são consideradas conectadas antes da escolha dos novos cabos. |

Para duas casas `i` e `j`, localizadas em `(xi, yi)` e `(xj, yj)`, o comprimento da nova ligação é:

$$
d(i,j)=\sqrt{(x_j-x_i)^2+(y_j-y_i)^2}
$$

As conexões já disponíveis **não significam que a distância física entre as casas seja zero**: significam apenas que não é necessário gastar cabos novos para conectá-las.

### 1.4 Identificação da família do problema

O Treehouses pertence à família de **Árvore Geradora Mínima (Minimum Spanning Tree — MST)**, considerando as conexões preexistentes como componentes já unidas. A tarefa é escolher ligações adicionais que conectem todas as componentes com a **menor soma de pesos**.

Não buscamos o caminho mais curto entre duas casas específicas, mas sim o menor comprimento total para construir a rede inteira. Também não é um problema de fluxo máximo, pois não existem capacidades de transporte a serem maximizadas.

