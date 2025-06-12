import sys
input = sys.stdin.readline

# N 은 길이
N = int(input())

# MOD는 나눠야 할 큰수
MOD = 1000000000

# 기본값 세팅
dp = [
    [ 0 for _ in range(10) ] for _ in range(N+1)
]

# 1의 자리수는 다 1로 세팅
for default in range(1 , 10): # j는 끝나는 자릿수
    dp[1][default] = 1

for i in range(1,N):
    for j in range(10):
        if j > 0:
            dp[i+1][j-1] += dp[i][j]
            dp[i+1][j-1] %= MOD
        if j < 9:
            dp[i+1][j+1] += dp[i][j]
            dp[i+1][j+1] %= MOD

# for i in range(2 , N+1):
#     for j in range(10):
#         # 끝자리가 1일때만 0으로 갈수있음 계단수니까
#         if j == 0:
#             dp[i][j] = dp[i-1][j+1]
#             continue
#         # 끝자리가 8일때만 9로 갈수있음 계단수니까
#         if j == 9:
#             dp[i][j] = dp[i-1][j-1]
#             continue

#         # 나머진 앞뒤숫자로 끝날 때 올수있잖아?      
#         dp[i][j] = ((dp[i-1][j-1] % MOD) + (dp[i-1][j+1] % MOD)) % MOD

result = 0
for num in dp[N]:
    result = ((result % MOD) + (num % MOD)) % MOD

# print(dp)
print(result)