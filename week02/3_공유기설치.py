import sys
# 공유기의 거리를 이분탐색으로 나누면서 10 5 7 8 이런식으로 가장 많은 공유기를 설치할 수 있는 거리의 갯수를 구한다.

n,c = map(int,input().split(' '))

house = sorted([ int(sys.stdin.readline()) for _ in range(n)])

def binary_search():
    
    start = 1
    end = house[-1] - house[0]
    
    length = len(house)
    result = 0

    while start <= end:
        current = house[0]
        count = 1
        mid = ( start + end ) // 2

        for i in range(1, length):
            if house[i] >= current + mid:
                count += 1
                current = house[i]

        if count >= c:
            start = mid + 1
            result = mid
        else:
            end = mid - 1

    print(result)



binary_search()