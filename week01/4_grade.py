def solution():
    
    result = int(input())

    if result < 60:
        print('F')
    elif result >= 60 and result < 70:
        print('D')
    elif result >= 70 and result < 80:
        print('C')
    elif result >= 80 and result < 90:
        print('B')
    elif result >= 90 and result <= 100:
        print('A')

solution()

# 시간복잡도 O(1) n 값과 상관없이 고정된 상수연산횟수
# 공간복잡도 O(1) result 한개