def move(start,end):
    print(f"{start} {end}")

def hanoi(N, start, end, sub):
    if N == 1:
        move(start, end)
        return
    else:
        hanoi(N-1 , start, sub, end)
        move(start, end)
        hanoi(N-1, sub, end, start)

def solution():
    n = int(input())
    
    print(2**n - 1)

    if n <= 20: hanoi(n, 1, 3, 2)
    
        

solution()

# 1. 첫번째 재귀에서는 N 번째 원반을 목적지로 옮기기 위해 N-1 개의 원반을 경유지로 옮긴다.
# 2. 그 다음 N 번째 원반을 목적지로 옮긴다.
# 3. 경유지에 있는 N-1 개의 원반을 목적지로 옮긴다.


# 시간복잡도: OO