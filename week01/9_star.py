def solution():
    
    n = int(input())

    for i in range(1,n+1):
        print('*'*i)

solution()

# 시간복잡도 O(1) n 이 최대 100으로 고정되어있다. 그래서 상수시간! 
# 공간복잡도 O(1) 변수 n 을 저장하는 거 말고는 없다.