def solution():
    
    n = int(input())

    for i in range(1,10):
        print(f"{n} * {i} = {n*i}")

solution()

# 시간복잡도 O(1) n 값과 관계없이 9번의 연산을 가짐
# 공간복잡도 O(1) n 값과 관계없이 n 하나만을 차지함