def solution():
    
    year = int(input())

    print(1) if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0) else print(0)
    

solution()

# 시간복잡도 O(1) n 값과 상관없이 고정된 상수연산횟수
# 공간복잡도 O(1) year 한개