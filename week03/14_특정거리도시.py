from collections import defaultdict , deque

import sys
input = lambda: sys.stdin.readline().strip()

# N은 도시의 개수
# M 은 도로의 개수
# 거리정보 K
# 출발도시의 번호 X

N,M,K,X = map(int, input().split(' '))

# 도시 도로정보 세팅
citys = defaultdict(list)

for _ in range(M):
    u,v = map(int, input().split(' '))

    citys[u].append(v)


# 방문정보
visited = [ False for _ in range(N+1) ]
distance = [ 0 for _ in range(N+1) ]
result = []

def bfs(result,start):

    queue = deque()
    queue.append(start)
    visited[start] = True

    while queue:
        city = queue.popleft()

        for i in citys[city]:
            if not visited[i]:
                current_distance = distance[city] + 1
                
                visited[i] = True
                distance[i] = current_distance

                if current_distance == K: result.append(i)

                queue.append(i)

bfs(result,X)

if result:
    for i in sorted(result):
        print(i)
else:
    print(-1)