# 2차원 배열 ( 고정 입력 )
grid = [
    [6,8,2,6,2],
    [3,2,3,4,6],
    [6,7,3,3,2],
    [7,2,5,3,6],
    [8,9,5,2,7]
]

N = len(grid)
rain_height = 5 # 비의 높이 고정

# 방문 체크 배열
visited = [[False] * N for _ in range(N)]

# 상하좌우 방향 정의
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# DFS 함수
def dfs(x,y):
    visited[x][y] = True

    for i in range(4):
        nx,ny = x + dx[i] , y + dy[i]

        if 0 <= nx < N and 0 <= ny < N:
            if not visited[nx][ny] and grid[nx][ny] > rain_height:
                dfs(nx,ny)


# 안전영역 개수 세기
safe_area_count = 0

for i in range(N):
    for j in range(N):
        if not visited[i][j] and grid[i][j] > rain_height:
            dfs(i,j)
            safe_area_count += 1

print(safe_area_count)