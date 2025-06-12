import sys
input = sys.stdin.readline

# N은 도시의 개수
N = int(input())

# 도시 간 이동 비용 행렬
city = [
    list(map(int, input().strip().split())) for _ in range(N)
]

# DP 배열 초기화
# dp[current][visited] = 현재 current 도시에 있고, visited 상태일 때의 최소 비용
dp = [
    [-1] * (1 << N) for _ in range(N)
    ]

print(city)
print(dp)

# def tsp(current, visited):
#     # 모든 도시를 방문했다면
#     if visited == (1 << N) - 1:
#         # 시작 도시로 돌아갈 수 있는 경우
#         if city[current][0] != 0:
#             return city[current][0]
#         return float('inf')
    
#     # 이미 계산된 경우
#     if dp[current][visited] != -1:
#         return dp[current][visited]
    
#     # 최소 비용 초기화
#     min_cost = float('inf')
    
#     # 다음 도시 선택
#     for next_city in range(N):
#         # 아직 방문하지 않은 도시이고, 현재 도시에서 다음 도시로 갈 수 있는 경우
#         if not visited & (1 << next_city) and city[current][next_city] != 0:
#             # 다음 도시로 이동하는 비용 계산
#             cost = city[current][next_city] + tsp(next_city, visited | (1 << next_city))
#             min_cost = min(min_cost, cost)
    
#     # 결과 저장
#     dp[current][visited] = min_cost
#     return min_cost

# # 0번 도시에서 시작
# print(tsp(0, 1))

# # print(dp)