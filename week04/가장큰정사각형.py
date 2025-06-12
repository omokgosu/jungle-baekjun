import sys
input = sys.stdin.readline

# N,M 은 이차원 배열의 크기
N,M = map( int, input().strip().split() )

rectangle = [
  list(map(int,(list(input().strip()))))  for _ in range(N)
]

# dp = [
#     [ 0 ] * M for _ in range(N)
# ]

result = 0
for i in range(N):
    for j in range(M):
        if i == 0 or j == 0:
            result = max( rectangle[i][j] , result )
            continue

        if rectangle[i][j] == 0:
            continue
        
        a = rectangle[i-1][j-1]
        b = rectangle[i][j-1]
        c = rectangle[i-1][j]

        rectangle[i][j] = min(a,b,c) + 1

        result = max(result , rectangle[i][j])

# print(rectangle)
print(result * result)