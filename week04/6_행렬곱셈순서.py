# import sys
# input = lambda: sys.stdin.readline().strip()

# sys.setrecursionlimit(10 ** 9)

# # N은 행렬의 갯수
# N = int(input())

# # 예시 행렬
# matrix = [ tuple(map(int, input().split(' '))) for _ in range(N) ]

# dp = [
#     [ -1 for _ in range(N) ] for _ in range(N)
# ]

# def multiple(start,end):
#     if dp[start][end] != -1: # 이미 계산된 경우
#         return dp[start][end]
    
#     if start == end: # 행렬이 하나인 경우
#         return 0
    
#     if start + 1 == end: # 행렬의 차이가 하나인 경우
#         return matrix[start][0] * matrix[start][1] * matrix[end][1]

#     ## 행렬이 3개 이상일 때
#     result = float('Inf')
#     for i in range(start,end):
#         a = matrix[start][0] * matrix[i][1] * matrix[end][1]
#         result = min( result , multiple(start,i) + multiple(i+1 ,end) + a )
    
#     dp[start][end] = result
#     return result

# print( multiple( 0, len(matrix) - 1 ) )

import sys
input = sys.stdin.readline

N = int(input())
sizes = [tuple(map(int, input().split())) for _ in range(N)]

memo = [[0] * (N) for _ in range(N)]

def find_answer():
    for gap in range(1, N):
        for i in range(N - gap):
            j = i + gap
            temp = float('inf')
            
            for k in range(i, j):
                cost = memo[i][k] + memo[k + 1][j] + sizes[i][0] * sizes[k][1] * sizes[j][1]
                
                if cost < temp:
                    temp = cost
            
            if i == 0 and j == (N - 1):
                return temp
            memo[i][j] = temp
                   
print(find_answer())