import math

def solution():
    
    a,b = map(int , input().split(' '));
    
    print(a+b)
    print(a-b)
    print(a*b)
    print(math.trunc(a/b))
    print(a%b)
    

solution()

# 시간복잡도 o(1)  
# 상수횟수이니까! N 에 비례해서 연산이 늘어나지 않는다. split 이 여러번 연산하니까 문자열이 길어지면 n 의길이에 따라 늘어나는거 아닐까?
# 하지만 입력제한이  A,와 B가 자연수 1과 10000 사이이므로 문자열 길이가 최대 11이다. 그러므로 상수시간으로 계산한다!
# 공간복잡도 o(1)  상수갯수니까 2개 고정이기 때문에