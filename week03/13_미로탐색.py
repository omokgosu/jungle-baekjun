from collections import deque

import sys
input = lambda: sys.stdin.readline().strip()

# N,M 은 도착지점
N,M = map(int, input().split(' '))

# 미로생성
MAZE = []

for i in range (N):
    MAZE.append(  list(map(int,list(input()))) )

# 상하좌우
dx = [ -1 , 1 , 0 , 0 ]
dy = [  0 , 0 ,-1 , 1 ]

# BFS = Breadth first search 너비우선탐색
# 노드가 갈수있는 곳을 체크하면서 이동

def bfs():

    # x좌표 , y좌표, 거리
    queue = deque()
    queue.append((0,0))

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]

            # 미로 범위 벗어남
            if next_x < 0 or next_y < 0 or next_x >= N or next_y >= M:
                continue

            # 벽이면 무시 즉 0
            if MAZE[next_x][next_y] == 0:
                continue

            # 처음 방문하면 최단거리
            if MAZE[next_x][next_y] == 1:
                MAZE[next_x][next_y] = MAZE[x][y] + 1
                queue.append((next_x,next_y))

    return MAZE[N-1][M-1]

print(bfs())