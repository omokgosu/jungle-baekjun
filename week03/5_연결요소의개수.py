from collections import defaultdict , deque

import sys
# sys.setrecursionlimit(10**9)
input = lambda: sys.stdin.readline().strip()

# N 은 정점의 개수
# M 은 간선의 개수
N,M = map(int,input().split(' '))

# 그래프 노드
graph = defaultdict(list)

for i in range(M):
    u,v = map(int,input().split(' '))

    graph[u].append(v)
    graph[v].append(u)


visited = [ False for _ in range(N+1) ]

# 재귀버전
# def dfs(start):
#     visited[start] = True
    
#     for i in graph[start]:
#         if not visited[i]:
#             visited[i] = True
#             dfs(i)

# 스택버전
def dfs(start):
    stack = deque([start])

    while stack:
        v = stack.popleft()

        if not visited[v]:
            visited[v] = True

            for i in graph[v]:
                if not visited[i]:
                    stack.append(i)


# 연결요소 갯수세기
count = 0
for i in range(1,N+1):
    if not visited[i]:
        count += 1
        dfs(i)

print(count)