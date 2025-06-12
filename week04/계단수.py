import sys
input = sys.stdin.readline

# N은 길이
N = int(input())

# MOD 는 나눠야 할 큰 수
MOD = 1000000000

# dp 테이블 초기화
dp = [ [ [0] * (1 << 10) for _ in range(10) ] for _ in range(N+1) ]

# 0 제외
for i in range(1,10):
    dp[1][i][1 << i] = 1

# 자리수
for i in range(1,N):
    # 숫자범위 j
    for j in range(10):
        # 비트마스킹
        for k in range(1 << 10):
            # 맨 뒤에 있는 수자가 0보다 크면 해당 숫자보다 1 작은 숫자들이 올 수 있음
            if j > 0:
                next = k | (1 << (j - 1))
                dp[i+1][j-1][next] += dp[i][j][k]
                dp[i+1][j-1][next] %= MOD
            if j < 9:
                next = k | (1 << (j + 1))
                dp[i+1][j+1][next] += dp[i][j][k]
                dp[i+1][j+1][next] %= MOD

result = 0
for i in range(10):
    result += dp[N][i][(1 << 10) - 1]
    result %= MOD

print(result)