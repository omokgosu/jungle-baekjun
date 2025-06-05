from collections import defaultdict
import sys

input = lambda: sys.stdin.readline().strip()

sys.setrecursionlimit(10**9)



# 정점의 수 N
N = int(input())

# 실내인지 실외인지 쳌디사운드
is_indoor = [0] + list(input())

graph = defaultdict(list)

# 셋째줄부터 N+1 까지 입력받음
for _ in range(2,N+1):
    u,v = map(int, input().split(' '))

    graph[u].append(v)
    graph[v].append(u)

# 무한루프방지 방문배열
visited = [ False for _ in range(N+1)]
def dfs(start):

    global count
    # 현재노드 방문표시
    visited[start] = True

    # 현재노드와 이어진 간선들
    for i in graph[start]:
        # 만약 이어진 간선을 방문한 적이없고, 이어진 간선이 실내면 count 를 더하고 다른곳을 방문한다.
        if is_indoor[i] == '1' and not visited[i]:
            count += 1
            continue

        # 만약 이어진 간선을 방문한 적이 없고, 이어진 간선이 실외면 count 를 dfs 에 더한다.
        if is_indoor[i] == '0' and not visited[i]:
            dfs(i)


count = 0

# 1부터 N 번째 노드까지 전부 순회한다.
for i in range(1,N+1):
    # 실내인 경우만 탐색을 하도록 한다.
    if is_indoor[i] == '1':
        dfs(i)

    # 모든 노드마다 체크해야 하므로 방문을 초기화해서 다 방문할 수 있도록 한다.
    visited = [ False for _ in range(N+1) ]
    

print(count)