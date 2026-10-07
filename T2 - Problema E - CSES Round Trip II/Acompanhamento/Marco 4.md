# Marco 4 — Implementação final e conclusão

## 1. Solução final

A solução final do problema **CSES Round Trip II** foi desenvolvida em **Python**, utilizando como base as implementações de referência disponibilizadas na disciplina na biblioteca `algs4-py`.

As principais referências utilizadas foram:

- `directed_cycle.py`;
- `digraph.py`;
- `bag.py`.

A estratégia principal permanece baseada em uma **Busca em Profundidade (DFS) recursiva** para detectar a existência de um ciclo em um grafo dirigido.

A solução utiliza as seguintes estruturas:

```text
marked[]
on_stack[]
edge_to[]
cycle
```

O ciclo é detectado quando, durante a DFS, uma aresta alcança um vértice que ainda pertence ao caminho ativo da busca:

```text
on_stack[w] = True
```

Nesse caso, o vetor `edge_to[]` é utilizado para reconstruir os vértices pertencentes ao ciclo.

---

## 2. Implementações reutilizadas

### `directed_cycle.py`

A principal lógica algorítmica foi baseada na implementação `directed_cycle.py`.

Foram preservados os seguintes elementos:

```text
marked[]
on_stack[]
edge_to[]
DFS recursiva
detecção por on_stack
reconstrução do ciclo
```

A DFS marca um vértice como visitado e como ativo no caminho atual:

```python
self._marked[v] = True
self.on_stack[v] = True
```

Quando encontra um vizinho ainda não visitado, registra o caminho:

```python
self.edge_to[w] = v
self.dfs(G, w)
```

Quando encontra um vértice que ainda está no caminho ativo:

```python
elif self.on_stack[w]:
```

é identificado um ciclo dirigido.

---

### `digraph.py`

A implementação `digraph.py` foi utilizada como referência para representar o grafo dirigido.

Cada vértice possui uma lista de adjacência contendo somente os vértices alcançáveis diretamente a partir dele.

Assim, uma aresta:

```text
v → w
```

é adicionada apenas à lista de adjacência de `v`.

Esse comportamento é adequado ao problema, pois todos os voos são de sentido único.

---

### `bag.py`

A estrutura `Bag` é utilizada pela implementação original de `Digraph` para armazenar os elementos das listas de adjacência.

Na solução adaptada, sua função foi mantida como estrutura auxiliar da representação do grafo.

---

## 3. Alterações realizadas

As implementações de referência foram adaptadas para funcionar no formato exigido pelo **CSES Round Trip II**.

As principais alterações foram:

### 3.1 Entrada

A implementação original lê dados de arquivos utilizados nos exemplos da biblioteca.

Na solução final, a entrada foi adaptada para a entrada padrão utilizada pelo CSES.

A primeira linha contém:

```text
n m
```

onde:

- `n` é o número de cidades;
- `m` é o número de voos.

As próximas `m` linhas possuem:

```text
a b
```

representando o voo dirigido:

```text
a → b
```

---

### 3.2 Numeração dos vértices

O CSES utiliza cidades numeradas de:

```text
1 até n
```

Enquanto a implementação de referência trabalha naturalmente com:

```text
0 até V - 1
```

Por isso, durante a leitura foi utilizada a conversão:

```python
a = a - 1
b = b - 1
```

Na saída é realizada a operação inversa:

```python
v + 1
```

Dessa forma, internamente é mantido o padrão utilizado pelas implementações de referência, mas a resposta permanece no formato esperado pelo CSES.

---

## 4. Adaptação da saída

Na implementação de referência, o algoritmo apenas informa ou apresenta o ciclo encontrado.

O CSES exige primeiro a quantidade de cidades presentes na rota:

```text
k
```

e depois a sequência de cidades:

```text
cidade1 cidade2 ... cidadek
```

Caso nenhum ciclo seja encontrado, deve ser impresso:

```text
IMPOSSIBLE
```

Por isso a saída foi adaptada para:

```python
if not finder.has_cycle():
    print("IMPOSSIBLE")
else:
    resposta = [v + 1 for v in finder.cycle]

    print(len(resposta))
    print(*resposta)
```

---

## 5. Reconstrução do ciclo

Quando a DFS encontra uma aresta:

```text
v → w
```

com:

```text
on_stack[w] = True
```

é identificado um ciclo.

Nesse momento, a reconstrução utiliza:

```text
edge_to[]
```

para percorrer os vértices anteriormente visitados.

Considere, por exemplo:

```text
0 → 2 → 1
```

com:

```text
edge_to[2] = 0
edge_to[1] = 2
```

Se for encontrada a aresta:

```text
1 → 0
```

o algoritmo recupera o caminho anterior e forma:

```text
0 → 2 → 1 → 0
```

O primeiro vértice aparece novamente no final para indicar que a viagem retorna à cidade inicial.

---

## 6. Funcionamento do `on_stack`

O vetor:

```text
marked[]
```

indica se um vértice já foi visitado em algum momento.

Já:

```text
on_stack[]
```

indica se o vértice ainda pertence ao caminho atual da DFS.

Por exemplo, durante a exploração:

```text
0 → 2 → 1
```

temos:

```text
on_stack[0] = True
on_stack[2] = True
on_stack[1] = True
```

Caso seja encontrada a aresta:

```text
1 → 0
```

o valor:

```text
on_stack[0] = True
```

indica que o vértice `0` ainda faz parte do caminho atual.

Portanto, a aresta fecha:

```text
0 → 2 → 1 → 0
```

e comprova a existência de um ciclo dirigido.

Quando a exploração de um vértice termina normalmente, ele deixa de fazer parte do caminho ativo:

```python
self.on_stack[v] = False
```

---

## 7. Tratamento de componentes desconexas

O grafo pode possuir várias componentes.

Por esse motivo, uma única DFS iniciada em um vértice não necessariamente alcançará todas as cidades.

A implementação percorre todos os vértices:

```python
for v in range(G.V):
    if not self._marked[v]:
        self.dfs(G, v)
```

Assim, caso um vértice ainda não tenha sido visitado, uma nova DFS é iniciada.

Dessa forma, um ciclo pode ser encontrado mesmo que esteja localizado em outra parte desconexa do grafo.

---

## 8. Limite de recursão

A implementação de referência utiliza uma DFS recursiva.

Como o problema permite até:

```text
10^5 vértices
```

foi necessário aumentar o limite de chamadas recursivas do Python.

Foi utilizado:

```python
sys.setrecursionlimit(300000)
```

Essa alteração permite que a DFS percorra caminhos mais profundos do que o limite padrão do Python.

---

## 9. Encerramento após encontrar o ciclo

O problema exige apenas um ciclo válido.

Por esse motivo, quando um ciclo é encontrado, não é necessário continuar procurando outros ciclos.

Durante a DFS é utilizada a verificação:

```python
if self.has_cycle():
    return
```

Assim, a busca pode ser interrompida após encontrar uma resposta válida.

Essa modificação não altera a complexidade de pior caso, mas pode evitar processamento desnecessário.

---

## 10. Casos de teste

Para verificar a implementação foram considerados diferentes tipos de entrada.

### Teste 1 — Exemplo oficial

Entrada:

```text
4 5
1 3
2 1
2 4
3 2
3 4
```

Existe o ciclo:

```text
1 → 3 → 2 → 1
```

Uma saída válida é:

```text
4
1 3 2 1
```

Também podem existir outras formas válidas de apresentar o mesmo ciclo, desde que a direção das arestas seja respeitada.

---

### Teste 2 — Grafo sem ciclo

Entrada:

```text
4 3
1 2
2 3
3 4
```

Nesse caso temos apenas:

```text
1 → 2 → 3 → 4
```

Não existe nenhuma aresta que retorne para um vértice anterior.

Saída esperada:

```text
IMPOSSIBLE
```

---

### Teste 3 — Ciclo em outra componente

Entrada:

```text
6 4
1 2
3 4
4 5
5 3
```

Os vértices `1` e `2` não formam ciclo.

Entretanto:

```text
3 → 4 → 5 → 3
```

forma um ciclo válido.

Uma saída possível é:

```text
4
3 4 5 3
```

Esse teste confirma que a busca percorre também componentes desconexas.

---

### Teste 4 — Ciclo de dois vértices

Entrada:

```text
3 2
1 2
2 1
```

Existe:

```text
1 → 2 → 1
```

Uma saída válida é:

```text
3
1 2 1
```

---

### Teste 5 — Grafo maior sem ciclo

Entrada:

```text
6 6
1 2
1 3
2 4
3 4
4 5
5 6
```

Todas as arestas avançam pelo grafo sem retornar para um vértice ativo.

Saída esperada:

```text
IMPOSSIBLE
```

---

## 11. Complexidade de tempo

A DFS visita cada vértice no máximo uma vez.

Além disso, cada aresta do grafo é analisada durante a exploração das listas de adjacência.

Portanto:

```text
Tempo = O(V + E)
```

onde:

- `V` é a quantidade de vértices;
- `E` é a quantidade de arestas.

No pior caso, o algoritmo precisará percorrer todo o grafo antes de encontrar um ciclo ou concluir que nenhum ciclo existe.

---

## 12. Complexidade de espaço

A representação do grafo por listas de adjacência utiliza:

```text
O(V + E)
```

As estruturas auxiliares:

```text
marked[]
on_stack[]
edge_to[]
```

utilizam:

```text
O(V)
```

A lista utilizada para armazenar o ciclo também pode ocupar:

```text
O(V)
```

Como a DFS é recursiva, a pilha de chamadas pode atingir:

```text
O(V)
```

no pior caso.

Assim:

```text
Memória auxiliar = O(V)
```

Considerando também a representação do grafo:

```text
Memória total = O(V + E)
```

---

## 13. Relação entre as implementações de referência e a solução final

| Implementação de referência | Utilização na solução |
|---|---|
| `directed_cycle.py` | Base da DFS, detecção e reconstrução do ciclo |
| `digraph.py` | Base da representação do grafo dirigido |
| `bag.py` | Estrutura auxiliar da lista de adjacência |
| `_marked[]` | Mantido para controle dos vértices visitados |
| `on_stack[]` | Mantido para identificar o caminho ativo |
| `edge_to[]` | Mantido para reconstrução do ciclo |
| `cycle` | Mantido para armazenar a resposta |

As principais alterações foram relacionadas à entrada, saída, numeração das cidades e limites de execução.

A lógica estrutural utilizada para detectar o ciclo foi preservada.

---

## 14. Organização da solução

A solução final será armazenada no diretório:

```text
src/
```

contendo o arquivo principal:

```text
main.py
```

As partes necessárias das implementações de referência foram incorporadas à solução para permitir sua execução de forma independente.

Essa organização permite que o programa seja executado diretamente utilizando:

```bash
python main.py
```

com a entrada fornecida pela entrada padrão.

---

## 15. Resultado da submissão

A solução deverá ser submetida ao problema:

```text
CSES Round Trip II
```

Após a submissão, deverá ser registrado o resultado obtido.

### Resultado

```text
[INSERIR AQUI O RESULTADO DA SUBMISSÃO]
```

Quando a plataforma retornar:

```text
Accepted
```

a evidência deverá ser salva em:

```text
evidencias/accepted.png
```

ou:

```text
evidencias/accepted.pdf
```

---

## 16. Evidência do Accepted

Após a aprovação da solução, inserir nesta seção a evidência da submissão.

Exemplo:

```md
![Accepted no CSES](../evidencias/accepted.png)
```

---

## 17. Conclusão

A solução final do problema **CSES Round Trip II** foi baseada nas implementações Python de referência disponibilizadas na disciplina.

A estrutura `digraph.py` foi utilizada como referência para representar o grafo dirigido e `directed_cycle.py` forneceu a estratégia principal de detecção de ciclos utilizando DFS recursiva.

O critério fundamental utilizado pelo algoritmo é:

```text
on_stack[w] = True
```

Quando uma aresta alcança um vértice que ainda está ativo na DFS, é identificada uma aresta de retorno e, consequentemente, um ciclo dirigido.

O vetor `edge_to[]` permite reconstruir a sequência de vértices pertencentes ao ciclo.

As adaptações realizadas preservam a lógica das implementações de referência e adequam a solução ao formato exigido pelo CSES.

A solução apresenta:

```text
Complexidade de tempo: O(V + E)

Memória auxiliar: O(V)

Memória total: O(V + E)
```

A conclusão do marco ocorrerá após a obtenção do resultado `Accepted` e o registro da respectiva evidência no repositório.
