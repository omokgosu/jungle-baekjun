def solution():
    
    x,y,w,h = map( int , input().split(' ') )
    
    print (
        min(
            min(abs(w-x),abs(x-0)),
            min(abs(h-y),abs(y-0))
        )
    )

solution()

# 시간복잡도 O(1) n 값과 관계없이 빼기연산 2번 비교연산 3번을 가집
# 공간복잡도 O(1) x,y,w,h 4개기 떄문에 n값과 관계없이 상수