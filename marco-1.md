# Problema dos Dominós (Dominoes 2)

O problema apresenta um conjunto de dominós em que a queda de um dominó pode provocar a queda de outro. Além disso, existem alguns dominós que são derrubados de maneira manual, iniciando reações em cadeia.

## Objetivo
Determinar a quantidade total de dominós que caíram, somando os que foram derrubados manualmente com aqueles que caíram em consequência das reações em cadeia (efeito dominó).

## Especificação da Entrada
A primeira linha da entrada contém um inteiro que representa a **quantidade de casos de teste**. Para cada caso de teste, os dados são estruturados da seguinte forma:

### 1. Parâmetros Iniciais
Uma linha contendo três números inteiros: **N**, **M** e **L**.
* **`N`**: O número total de peças de dominó.
* **`M`**: O número de conexões (relações de causa e efeito) entre as peças.
* **`L`**: O número de dominós que foram derrubados manualmente.

### 2. Conexões (Causa e Efeito)
As próximas **`M`** linhas contêm **2 valores inteiros** cada, representando as conexões feitas entre as peças (ex: se a primeira peça cair, a segunda peça também cai).

### 3. Ações Manuais
Por fim, as **`L`** linhas seguintes contêm **1 inteiro** cada, indicando especificamente quais dominós foram derrubados com a mão no início.

## Especificação da Saída
Para cada caso de teste, deve ser apresentada em uma única linha a **quantidade total de dominós que caíram**.

## Restrições e Regras Importantes
* O número de peças, conexões e ações manuais (`N`, `M` e `L`) pode ser de **até 10.000**.
