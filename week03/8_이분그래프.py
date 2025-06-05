from collections import defaultdict

import sys

input = lambda: sys.stdin.readline().strip()

sys.setrecursionlimit(10**9)

# 테스트 케이스의 갯수 K
K = int(input())

for _ in range(K):
    # 그래프 정점의 개수 V
    # 그래프 간선의 개수 E
    V,E = map(int,input().split(' '))

    # 간선 정보 저장
    graph = defaultdict(list)
    visited = [ False for _ in range(V+1) ]
    color = [ 'white' for _ in range(V+1)]

    for i in range(E):
        u,v = map(int,input().split(' '))

        graph[u].append(v)
        graph[v].append(u)


    def dfs( start , current_color ):

        current_color = 'blue' if current_color == 'red' else 'red'

        visited[start] = True
        color[start] = current_color
        check = 'YES'

        for i in graph[start]:
            if color[i] == current_color:
                check = 'NO'
                return check
            
            if not visited[i]:
                visited[i] = True
                check = dfs( i, current_color)
        
        return check
    
    value = ''

    for i in range(1,V+1):
        if not visited[i]:
            value = dfs(i,'red')
        if value == 'NO': break
    
    print(value)



# 지피티한테 물어본 코드 가독성 개선버전
# import sys
# from collections import defaultdict

# input = lambda: sys.stdin.readline().strip()
# sys.setrecursionlimit(10**9)

# K = int(input())  # 테스트 케이스 개수

# for _ in range(K):
#     V, E = map(int, input().split())

#     graph = defaultdict(list)
#     visited = [False] * (V + 1)
#     color = [None] * (V + 1)  # None: 미정, 0: 빨강, 1: 파랑

#     for _ in range(E):
#         u, v = map(int, input().split())
#         graph[u].append(v)
#         graph[v].append(u)

#     def dfs(node, c):
#         visited[node] = True
#         color[node] = c

#         for neighbor in graph[node]:
#             if not visited[neighbor]:
#                 if not dfs(neighbor, 1 - c):  # 색 번갈아가며 탐색
#                     return False
#             elif color[neighbor] == c:
#                 return False  # 인접 정점과 색이 같으면 실패
#         return True

#     is_bipartite = True
#     for i in range(1, V + 1):
#         if not visited[i]:
#             if not dfs(i, 0):  # 0: 빨강, 1: 파랑
#                 is_bipartite = False
#                 break

#     print("YES" if is_bipartite else "NO")
