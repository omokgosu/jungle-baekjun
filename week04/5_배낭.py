import sys
input = lambda: sys.stdin.readline().strip()

# N 은 물품의 수
# K 는 준서가 버틸 수 있는 무게
N,K = map(int, input().split(' '))

product = sorted( list(map(int,input().split(' '))) for _ in range(N))
dp = [ [0 for _ in range(K+1)] for _ in range (N+1) ]

for i in range(1,len(product)+1):
    weight , value = product[i-1]

    for j in range(K+1):

        if j >= weight:
            dp[i][j] = max( value + dp[i-1][j-weight] , dp[i-1][j] )
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][K])