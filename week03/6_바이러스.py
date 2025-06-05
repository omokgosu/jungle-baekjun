from collections import defaultdict , deque

import sys
input = lambda: sys.stdin.readline().strip()

# 컴퓨터의 갯수
N = int(input())

# 네트워크의 갯수
M = int(input())

# 컴퓨터 인접리스트
computers = defaultdict(list)

for _ in range(M):
    u,v = map(int, input().split(' '))

    computers[u].append(v)
    computers[v].append(u)
    
# 방문정보
visited = [ False for _ in range(N+1) ]

def dfs(count , start):

    visited[start] = True

    for i in computers[start]:
        if not visited[i]:
            count = dfs(count , i)

    count += 1
    return count

count = dfs(0 , 1)

print(count - 1)