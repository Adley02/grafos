import sys

sys.setrecursionlimit(20000)


class Digraph:
    def __init__(self, v):
        self.V = v
        self.E = 0

        self.adj = [[] for _ in range(self.V)]

    def add_edge(self, v, w):

        self.adj[v].append(w)
        self.E += 1


class DepthFirstSearch:
    def __init__(self, G):

        self.marked = [False for _ in range(G.V)]


        self.count = 0

    def dfs(self, G, v):

        self.marked[v] = True


        self.count += 1


        for w in G.adj[v]:


            if not self.marked[w]:
                self.dfs(G, w)


def main():


    T = int(input())

    for _ in range(T):

        # n = número de dominós
        # m = número de relações
        # l = número de dominós derrubados manualmente
        n, m, l = map(int, input().split())


        G = Digraph(n)


        for _ in range(m):

            x, y = map(int, input().split())

            x -= 1
            y -= 1


            G.add_edge(x, y)


        search = DepthFirstSearch(G)


        for _ in range(l):

            z = int(input())


            z -= 1


            if not search.marked[z]:
                search.dfs(G, z)


        print(search.count)


if __name__ == "__main__":
    main()

