def is_hansu(n):

    if ( n < 100 ): return True

    arr =  list(map(int, str(n)))

    for i in range(2 , len(arr)):
        if  arr[i] - arr[i-1] == arr[i-1] - arr[i-2]: continue
        else: return False

    return True


def solution():
    
    num = input()
    count = 0
 
    for i in range(1, int(num)+1):
        if is_hansu(i): count += 1
   
    print(count)

solution()


# 시간복잡도 1 ~ 1000 까지
# 숫자 map list 변환 2m
# 수학연산 1
# O(n) 인데 1000 까지 정해져있으니까 상수연산