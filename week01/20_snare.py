import math

def solution():
    A,B,V = map(int, input().split(' '))
    print(math.ceil((V-B) / (A-B)))

solution()


# 시간복잡도 O(1) 계산한번!

# 공간복잡도 O(1) 공간 3개!