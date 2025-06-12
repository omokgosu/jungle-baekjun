import sys
input = lambda: sys.stdin.readline().strip()


N = int(input())

dp = [ 0 ] * ( max(3,N+1) )

dp[0] = 0
dp[1] = 1
dp[2] = 1

for i in range(3,N+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[N])