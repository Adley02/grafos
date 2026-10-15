# T2 — CSES Round Trip II

## 1. Identificação

**Disciplina:** Resolução de Problemas com Grafos  
**Professor:** Prof. Me. Ricardo Carubbi  
**Problema:** Problema E — CSES Round Trip II  
**Linguagem:** Python

### Integrantes

- Arthur Gomes de Aguiar - 1810460
- Guilherme Adley De Souza Batista - 2020670
---

## 2. Problema

O problema **CSES Round Trip II** apresenta um conjunto de cidades conectadas por voos de sentido único.

O objetivo é encontrar uma rota que:

1. comece em uma cidade;
2. percorra uma ou mais cidades;
3. respeite o sentido dos voos;
4. retorne à cidade inicial.

Portanto, o problema consiste em verificar a existência de um **ciclo em um grafo dirigido** e, caso exista, apresentar uma sequência de cidades que forme esse ciclo.

Caso não exista nenhum ciclo, o programa deve imprimir:

```text
IMPOSSIBLE
```

O problema não exige encontrar o menor ciclo. Qualquer ciclo dirigido válido pode ser apresentado.

---

## 3. Modelagem do grafo

O problema foi modelado como um **grafo dirigido e não ponderado**.

- Cada cidade corresponde a um vértice.
- Cada voo corresponde a uma aresta dirigida.
- Um voo de `a` para `b` é representado por:

```text
a → b
```

A direção é importante, pois a existência de:

```text
a → b
```

não implica necessariamente a existência de:

```text
b → a
```

O grafo pode ainda ser desconexo, portanto é necessário garantir que todos os vértices não visitados possam iniciar uma nova DFS.

---

## 4. Propriedade estrutural

A propriedade estrutural central é a existência de um **ciclo dirigido**.

Um ciclo ocorre quando existe um caminho:

```text
v0 → v1 → v2 → ... → vk → v0
```

no qual todas as arestas são percorridas respeitando suas direções.

Para identificar essa propriedade foi utilizada uma **Busca em Profundidade (DFS)**.

---

## 5. Estratégia algorítmica

A solução utiliza uma **DFS recursiva**.

Durante a execução são mantidas as seguintes estruturas:

### `marked[]`

Indica se um vértice já foi visitado pela DFS.

```text
marked[v] = True
```

significa que o vértice `v` já foi visitado em algum momento.

### `on_stack[]`

Indica se o vértice ainda pertence ao caminho atualmente explorado pela DFS.

```text
on_stack[v] = True
```

significa que o vértice ainda está presente na cadeia ativa de chamadas da DFS.

### `edge_to[]`

Registra o vértice anterior utilizado para alcançar cada vértice.

Por exemplo:

```text
edge_to[2] = 0
```

indica que a DFS chegou ao vértice `2` a partir do vértice `0`.

Essa estrutura é utilizada posteriormente para reconstruir o ciclo.

---

## 6. Critério para detectar o ciclo

Durante a DFS, considere uma aresta:

```text
v → w
```

Se `w` ainda não foi visitado, a DFS continua normalmente:

```python
if not marked[w]:
    edge_to[w] = v
    dfs(w)
```

Porém, caso `w` já tenha sido visitado e ainda esteja no caminho ativo:

```python
on_stack[w] == True
```

foi encontrada uma **aresta de retorno**.

Isso significa que a busca retornou para um vértice que ainda pertence ao caminho atual da DFS, comprovando a existência de um ciclo dirigido.

Por exemplo:

```text
0 → 2 → 1
```

se durante a exploração de `1` for encontrada a aresta:

```text
1 → 0
```

e:

```text
on_stack[0] = True
```

então existe o ciclo:

```text
0 → 2 → 1 → 0
```

---

## 7. Reconstrução do ciclo

Após identificar uma aresta de retorno, o vetor `edge_to[]` é utilizado para reconstruir os vértices percorridos.

Por exemplo:

```text
edge_to[2] = 0
edge_to[1] = 2
```

representa:

```text
0 → 2 → 1
```

Se a DFS encontrar:

```text
1 → 0
```

o caminho reconstruído será:

```text
0 → 2 → 1 → 0
```

O primeiro vértice é repetido no final para representar o fechamento do ciclo.

---

## 8. Implementações de referência

A solução foi desenvolvida a partir das implementações Python disponibilizadas na disciplina na biblioteca `algs4-py`.

As principais referências utilizadas foram:

### `directed_cycle.py`

Utilizado como principal referência para:

- DFS recursiva;
- controle dos vértices visitados;
- controle da pilha ativa;
- identificação de ciclos dirigidos;
- reconstrução do ciclo.

As principais estruturas preservadas foram:

```text
marked[]
on_stack[]
edge_to[]
cycle
```

### `digraph.py`

Utilizado como referência para a representação do grafo dirigido por meio de listas de adjacência.

Cada aresta:

```text
v → w
```

é armazenada somente na lista de adjacência de `v`.

### `bag.py`

Utilizado como referência para a estrutura auxiliar que armazena os vizinhos presentes nas listas de adjacência.

---

## 9. Alterações realizadas

A estratégia algorítmica das implementações de referência foi preservada.

As principais alterações realizadas foram necessárias para adaptar o código ao formato do **CSES Round Trip II**.

### 9.1 Entrada

A entrada foi adaptada para o formato:

```text
n m
a1 b1
a2 b2
...
am bm
```

onde:

- `n` representa o número de cidades;
- `m` representa o número de voos.

Na versão utilizada para testes locais, a leitura é realizada com `input()`:

```python
n, m = map(int, input().split())

for _ in range(m):
    a, b = map(int, input().split())
```

Essa escolha permite testar facilmente o programa pelo terminal e permanece compatível com o juiz online.

---

### 9.2 Conversão da numeração

O CSES utiliza cidades numeradas de:

```text
1 até n
```

Internamente, o `Digraph` utiliza índices:

```text
0 até n - 1
```

Por isso, na entrada é realizada a conversão:

```python
a -= 1
b -= 1
```

Na saída é feita a operação inversa:

```python
v + 1
```

Assim, a representação interna permanece compatível com o padrão utilizado pelas implementações de referência.

---

### 9.3 Saída

Caso nenhum ciclo seja encontrado:

```python
print("IMPOSSIBLE")
```

Caso exista um ciclo, são impressos:

1. a quantidade de vértices da rota;
2. os vértices pertencentes ao ciclo.

Exemplo:

```text
4
1 3 2 1
```

---

### 9.4 Limite de recursão

A implementação de referência utiliza DFS recursiva.

Como o problema pode possuir uma grande quantidade de vértices, o limite de recursão do Python foi aumentado:

```python
sys.setrecursionlimit(300000)
```

Essa alteração evita que caminhos muito profundos ultrapassem o limite padrão de chamadas recursivas da linguagem.

---

### 9.5 Componentes desconexas

O grafo pode ser desconexo.

Por isso, a solução verifica todos os vértices:

```python
for v in range(G.V()):
    if not marked[v]:
        dfs(v)
```

Dessa forma, caso um ciclo esteja em uma parte do grafo que não seja alcançável a partir do primeiro vértice, uma nova DFS será iniciada.

---

### 9.6 Encerramento após encontrar um ciclo

O problema aceita qualquer ciclo válido.

Portanto, depois que um ciclo é encontrado, não é necessário continuar procurando outros.

A busca pode ser encerrada antecipadamente:

```python
if self.has_cycle():
    return
```

Essa adaptação evita processamento desnecessário, embora a complexidade de pior caso permaneça a mesma.

---

## 10. Complexidade

### Complexidade de tempo

A DFS visita cada vértice no máximo uma vez.

Além disso, todas as arestas presentes nas listas de adjacência podem ser analisadas.

Assim:

```text
O(V + E)
```

onde:

- `V` é o número de vértices;
- `E` é o número de arestas.

---

### Complexidade de espaço

A representação do grafo por listas de adjacência ocupa:

```text
O(V + E)
```

As estruturas auxiliares:

```text
marked[]
on_stack[]
edge_to[]
```

ocupam:

```text
O(V)
```

A pilha de chamadas da DFS recursiva também pode chegar a:

```text
O(V)
```

no pior caso.

Portanto:

```text
Memória auxiliar = O(V)
```

e, considerando também a representação do grafo:

```text
Memória total = O(V + E)
```

---

## 11. Casos de teste

### Caso 1 — Grafo com ciclo

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

---

### Caso 2 — Grafo sem ciclo

Entrada:

```text
4 3
1 2
2 3
3 4
```

Saída:

```text
IMPOSSIBLE
```

---

### Caso 3 — Ciclo em outra componente

Entrada:

```text
6 4
1 2
3 4
4 5
5 3
```

A primeira componente não possui ciclo.

A segunda possui:

```text
3 → 4 → 5 → 3
```

Uma saída válida é:

```text
4
3 4 5 3
```

---

### Caso 4 — Ciclo com dois vértices

Entrada:

```text
3 2
1 2
2 1
```

Uma saída válida é:

```text
3
1 2 1
```

---

## 12. Casos especiais considerados

Foram considerados os seguintes casos:

- grafo sem ciclos;
- grafo desconexo;
- ciclo localizado em uma componente diferente da primeira;
- ciclo formado por poucos vértices;
- grafo com muitos vértices;
- vértices que já foram visitados, mas não estão mais no caminho ativo da DFS.

É importante destacar que:

```text
marked[v] = True
```

não é suficiente para identificar um ciclo.

O ciclo é reconhecido quando:

```text
on_stack[v] = True
```

pois isso indica que o vértice ainda pertence ao caminho atual da DFS.

---

## 13. Execução

O programa principal está localizado em:

```text
src/main.py
```

Para executar pelo terminal:

```bash
python src/main.py
```

Depois, informe a entrada.

Exemplo:

```text
4 5
1 3
2 1
2 4
3 2
3 4
```

Também é possível utilizar um arquivo de entrada.

No PowerShell:

```powershell
Get-Content input.txt | python src/main.py
```

---

## 14. Estrutura do projeto

```text
T2/
├── README.md
├── acompanhamento/
│   ├── marco-1.md
│   ├── marco-2.md
│   ├── marco-3.md
│   └── marco-4.md
├── src/
│   └── main.py
├── evidencias/
│   └── accepted.png
├── apresentacao/
│   └── apresentacao.pdf
└── dados/
    └── casos-de-teste.txt
```

---

## 15. Evidência do Accepted

Após a submissão da solução na plataforma CSES, a evidência do resultado deverá ser armazenada em:

```text
evidencias/accepted.png
```

A imagem pode ser exibida no README utilizando:

```md
![Accepted no CSES](evidencias/accepted.png)
```

**Status atual:** inserir o resultado real da submissão.

> Esta seção deverá ser atualizada somente após a plataforma confirmar o resultado `Accepted`.

---

## 16. Acompanhamento do trabalho

O desenvolvimento foi dividido em quatro marcos:

- **Marco 1:** compreensão do problema, modelagem e conhecimento prévio;
- **Marco 2:** componentes conexas e propriedades métricas de um caso adaptado não dirigido;
- **Marco 3:** definição e rastreamento da estratégia algorítmica;
- **Marco 4:** implementação final, adaptações e conclusão.

Os registros detalhados estão disponíveis no diretório:

```text
acompanhamento/
```

---

## 17. Uso de Inteligência Artificial

Durante o desenvolvimento do trabalho foi utilizada a ferramenta **ChatGPT**, da OpenAI, como recurso de apoio.

A ferramenta foi utilizada para:

- auxiliar na compreensão da DFS e das estruturas `marked`, `on_stack` e `edge_to`;
- apoiar a interpretação das implementações de referência do `algs4-py`;
- auxiliar na adaptação inicial do código para o formato do CSES;
- revisar explicações de complexidade de tempo e espaço;
- apoiar a organização e revisão dos arquivos de acompanhamento, README e apresentação.

As respostas geradas pela ferramenta foram analisadas, discutidas e adaptadas pelo grupo.

Os integrantes são responsáveis pela compreensão, implementação, testes e justificativas apresentadas no trabalho.

---

## 18. Conclusão

O problema **CSES Round Trip II** foi modelado como um grafo dirigido e resolvido utilizando uma DFS recursiva baseada nas implementações de referência da biblioteca `algs4-py`.

A principal propriedade utilizada para identificar o ciclo é a existência de uma aresta que alcança um vértice que ainda pertence ao caminho ativo da DFS:

```text
on_stack[w] = True
```

A estrutura `edge_to[]` permite reconstruir a sequência de vértices do ciclo encontrado.

A solução preserva a estratégia das implementações de referência e realiza adaptações relacionadas principalmente à entrada, saída, numeração dos vértices, limite de recursão e formato exigido pelo CSES.

A complexidade final da solução é:

```text
Tempo: O(V + E)
Memória auxiliar: O(V)
Memória total: O(V + E)
```
