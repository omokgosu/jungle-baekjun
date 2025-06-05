from collections import defaultdict

import sys
input = lambda: sys.stdin.readline().strip()

sys.setrecursionlimit(10**9)

# 노드의 갯수 1~N
N = int(input())

# 트리의 부모 배열


# 트리 상에서 연결된 두 정점
edges = sys.stdin.read().splitlines()
graph = defaultdict(list)

# 그래프
for i in edges:
    u,v = map(int,i.split(' '))

    graph[u].append(v)
    graph[v].append(u)

parent = [ i for i in range(N+1)]
visited = [ False for _ in range(N+1)]

def dfs(start):

    visited[start] = True
    
    for i in graph[start]:
        if not visited[i]:
            visited[i] = True
            parent[i] = start
            dfs(i)

for i in range(1,N+1):
    dfs(i)

for i in range(2, len(parent)):
    print(parent[i])