import sys
input = sys.stdin.readline

# N은 정수
N = int(input())

dp = [ float('Inf') ] * (N + 1)
dp[len(dp)-1] = 0

for i in range(N,0,-1):
    if i % 3 == 0:
        dp[i // 3] = min( dp[i // 3] , dp[i] + 1 )    
    if i % 2 == 0:
        dp[i // 2] = min( dp[i // 2] , dp[i] + 1 )
    
    dp[i-1] = min( dp[i-1] , dp[i] + 1 )

print(dp[1])
