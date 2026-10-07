import sys

# A DFS é recursiva e o grafo pode ter até 10^5 vértices
sys.setrecursionlimit(300000)


class Bag:
    def __init__(self):
        self._items = []

    def add(self, item):
        self._items.append(item)

    def __iter__(self):
        return iter(self._items)


class Digraph:
    def __init__(self, V):
        self._V = V
        self._E = 0
        self._adj = [Bag() for _ in range(V)]

    def V(self):
        return self._V

    def add_edge(self, v, w):
        self._adj[v].add(w)
        self._E += 1

    def adj(self, v):
        return self._adj[v]


class DirectedCycle:
    def __init__(self, G):
        self._marked = [False] * G.V()
        self.edge_to = [-1] * G.V()
        self.on_stack = [False] * G.V()
        self._cycle = None

        # Percorre todos os vértices porque o grafo pode ser desconexo
        for v in range(G.V()):
            if self.has_cycle():
                break

            if not self._marked[v]:
                self._dfs(G, v)

    def _dfs(self, G, v):
        self._marked[v] = True
        self.on_stack[v] = True

        for w in G.adj(v):
            if self.has_cycle():
                return

            if not self._marked[w]:
                self.edge_to[w] = v
                self._dfs(G, w)

            # Se w ainda está no caminho ativo, foi encontrado um ciclo
            elif self.on_stack[w]:
                path = []
                x = v

                # Reconstrói o ciclo usando edge_to
                while x != w:
                    path.append(x)
                    x = self.edge_to[x]

                path.append(w)
                path.reverse()

                # Repete o primeiro vértice para fechar o ciclo
                path.append(w)

                self._cycle = path
                return

        self.on_stack[v] = False

    def has_cycle(self):
        return self._cycle is not None

    def cycle(self):
        return self._cycle


def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))

    if not data:
        return

    n = data[0]
    m = data[1]

    G = Digraph(n)

    index = 2

    for _ in range(m):
        a = data[index] - 1
        b = data[index + 1] - 1
        index += 2

        G.add_edge(a, b)

    finder = DirectedCycle(G)

    if not finder.has_cycle():
        print("IMPOSSIBLE")
        return

    # Converte de 0...n-1 para 1...n
    answer = [v + 1 for v in finder.cycle()]

    print(len(answer))
    print(*answer)


if __name__ == "__main__":
    solve()
