def solution():
    
    n = int(input())

    for i in range(n):
        a,b = map( int , input().split(' ') )
        print(a+b)

solution()

# 시간복잡도 O(n) 입력받는 N에 따라 for 문의 연산횟수가 달라지므로 시간복잡도를 O(n) 으로 추측한다. 
# 공간복잡도 O(1) 반복바다 a,b 를 덮어쓰고 추가로 공간이 필요하지 않으므로 공간복잡도는 고정된 a,b 로 상수만큼 사용한다고 본다.