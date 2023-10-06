#finding C4 in graph in O(n^2)
# use augmented BFS
#let G be represented by adjacency list
from collections import deque
def bfs_visit(x,G,d,pi:list,theta):

    Q = deque()
    Q.append(x)
    d[x] = 0
    while Q:
        size = len(Q)
        for _ in range(size):
            v = Q.popleft()
            # if d[v] == 3:
            #     break
            # print("visi",v)
            # visited[v] = True
            for u in G[v] :
                if d[u] == d[v]-1:
                    pass # do nothing
                elif d[u] == float("inf"):
                    Q.append(u)
                    pi[u] = v
                    d[u] = d[v] + 1
                elif d[u] == d[v] + 1:
                    if pi[pi[u]] == pi[v]:
                   
                        return True
                elif d[u] == d[v] and theta[v] == theta[u] == -1:
                    theta[u] = v
                    theta[v] = u
                elif d[u] == d[v] and theta[v] != u:
                    #u is already matched
                    if theta[v] != -1:
                        c = theta[v]
                        if pi[c] == pi[u]:
                       
                            return True
                    if theta[u] != -1:
                        c = theta[u]
                        if pi[c] == pi[v]:
                            return True
    return False
                 
def BFS(G):
    n = len(G)
    # visited = [False for i in range(n)] # n is the number of vertices in G
    # d = [float("inf") for i in range(n)]
    # pi = [-1 for i in range(n)]
    # theta = [0 for i in range(n)]
    for i in range(n):
        d = [float("inf") for i in range(n)]
        pi = [-1 for i in range(n)]
        theta = [-1 for i in range(n)]
        if  bfs_visit(i,G,d,pi,theta):
            # print("d",d)
            # print("th",theta)
            # print("pi",pi)
            return True # graph G has C4
    # print("d",d)
    # print("th",theta)
    # print("pi",pi)
    return False
for _ in range(int(input())):
    n,m= map(int,input().split())
    L = [[] for i in range(n)]
    for i in range(m):
        a,b = map(int,input().split())
        L[a].append(b)
        L[b].append(a)
    print(BFS(L))


    




        
