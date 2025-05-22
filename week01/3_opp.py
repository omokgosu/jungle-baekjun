def solution():

    a = int(input())
    b = input()

    for i in range(1,4):
        print( a * int(b[-i]))

    print ( a * int(b) )

solution()


# 시간복잡도 O(1) 연산횟수가 N 값과 관계없이 고정되어있다.  for 문 고정 3번 연산 고정 4번
# 공간복잡도 O(1) a,b 랑 b 두개 상수만큼