import sys
input = lambda: sys.stdin.readline().strip()

# 테스트 케이스의 갯수
T = int(input())

for _ in range(T):
    # N 은 동전 종류 갯수
    N = int(input())
    # 동전 종류
    coins = list(map(int,input().split(' ')))

    # M은 만들어야 할 금액
    M = int(input())

    # 초기화
    dp = [ 1 ] + [ 0 ] * (M + 1)

    for coin in coins:
        for i in range(coin , M+1):
                dp[i] += dp[i-coin] 

    print(dp[M])

