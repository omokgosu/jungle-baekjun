import sys
input = sys.stdin.readline

# N 은 집의 개수
N = int(input())

rgb = [ 
    list(map(int,input().strip().split())) for _ in range(N)
]

dp = [
    [0] * 3 for _ in range(N)
]

dp[0] = rgb[0]

for i in range(1, len(rgb)):
    new_r,new_g,new_b = rgb[i]
    old_r,old_g,old_b = dp[i-1]

    dp[i][0] = min( new_r + old_g , new_r + old_b )
    dp[i][1] = min( new_g + old_r , new_g + old_b )
    dp[i][2] = min( new_b + old_r , new_b + old_g )

print(min(dp[N-1]))


