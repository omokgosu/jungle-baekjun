import sys
input = lambda: sys.stdin.readline().strip()

# 타일의길이
N = int(input())

# 큰수를 나눌 나머지
MOD = 15746

dp = [ 0 ] * ( max( 3 ,N + 1) )

dp[1] = 1
dp[2] = 2

# 모듈러 연산 = (a + b) % MOD = ((a % MOD) + (b % MOD)) % MOD

for i in range(3,N+1):
    dp[i] = ((dp[i-1] % MOD) + (dp[i-2] % MOD)) % MOD

print(dp[N])