from collections import defaultdict, deque

import sys
input = lambda: sys.stdin.readline().strip()


# N 은 정점의 개수
# M 은 간선의 개수
# V 는 시작노드
N,M,V = map(int,(input().split(' ')))

graph = defaultdict(list) # 빈거는 리스트로 기본 초기화

# 인접리스트 생성
for i in range(M):
    a , b = map(int,(input().split(' ')))
    graph[a].append(b)
    graph[b].append(a)

# 각 배열 정렬
for i in graph:
    graph[i].sort()



visited = [ False for _ in range(N+1)]

# 깊이우선탐색
# 재귀버전
# def dfs(start):
#     print(start,end=' ')
#     visited[start] = True

#     for i in graph[start]:
#         if not visited[i]:
#             dfs(i)

# 스택버전
def dfs(start):
    stack = deque([start])

    while stack:
        v = stack.pop()

        if not visited[v]:
            visited[v] = True
            print(v , end=' ')

            for i in reversed(graph[v]):
                if not visited[i]:
                    stack.append(i)

# 너비우선탐색
def bfs(start):
    queue = deque([start])
    visited[start] = False

    while queue:
        v = queue.popleft()
        print(v, end = ' ')

        for i in graph[v]:
            if visited[i]:
                visited[i] = False
                queue.append(i)

dfs(V)
print('')
bfs(V)
