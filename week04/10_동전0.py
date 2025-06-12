import sys
input = lambda: sys.stdin.readline().strip()

# N 은 동전의 갯수, K는 가치의 합
N,K = map(int,input().split(' '))

# coin 은 동전의 가치가 오름차순으로 정렬
coin = sorted([ int(input()) for _ in range(N) ], reverse=True )

result = 0
cul = K

for i in coin:
    
    # a = 몫 , b = 나머지
    a = cul // i
    b = cul % i

    result += a

    if b == 0: break

    cul -= i * a

print(result)