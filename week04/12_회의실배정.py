import sys
input = lambda: sys.stdin.readline().strip()


 # 회의 개수
N = int(input())

meeting = sorted( [ tuple(map(int, input().split(" "))) for _ in range(N) ] , key=lambda x: ( x[1] , x[0] ))

end_time = 0
count = 0

for meet in meeting:
    start , end = meet

    if start >= end_time:
        end_time = end
        count += 1

print(count)