from collections import defaultdict, deque

import sys
input = lambda: sys.stdin.readline().strip()

# N은 학생수 
# M은 비교횟수
N,M = map(int,input().split(' '))

# 진입차수 계산
graph = defaultdict(list)
inDegree = [ 0 for _ in range(N+1)]

# 그래프랑 진입차수 생성해주기
for _ in range(M):
    u,v = map(int,input().split(' '))

    graph[u].append(v)
    inDegree[v] += 1

# 처음 배열을 보고 진입차수가 0인애들 담아주기
queue = deque()
result = []

for i in range(1, N+1):
    if inDegree[i] == 0:
        queue.append(i)

while queue:
    x = queue.popleft()
    result.append(str(x))

    for node in graph[x]:
        inDegree[node] -= 1
        if inDegree[node] == 0:
            queue.append(node)

print(' '.join(result))