# 중간값을 찾으려면?
# 크기를 절반으로 나눠서
# 큰 쪽은  min heap으로 해서 최상단에 제일 작은 노드가 위치하고
# 작은 쪽은 max heap으로 해서 최상단에 제일 큰 노드가 위치하게하면
# min heap의 root 와 max heap 의 root 가 중간값이 됨

# 그리고 두 heap 의길이를 계속 같게해야함
# 왼쪽 오른쪽 왼쪽 오른쪽
# 

# max heap   min heap
#    5        5
#    5        7
#    2        10
#    1         
#    

import heapq
from sys import stdin
input=stdin.readline

max_heapq = [] # 절반으로 나눴을 때, 작은 값들
min_heapq = [] # 절반으로 나눴을 때, 큰 값들

# 총 반복 횟수
n = int(input())

for i in range(n):
    number = int(input())

    if min_heapq and number > min_heapq[0]:
        heapq.heappush(min_heapq , number)
    else:
        heapq.heappush(max_heapq , -number)

    max_len = len(max_heapq)
    min_len = len(min_heapq)

    if max_len - min_len == 2:
        heapq.heappush(min_heapq , -heapq.heappop(max_heapq))
        max_len -= 1
        min_len += 1
    if min_len - max_len == 2:
        heapq.heappush(max_heapq , -heapq.heappop(min_heapq))
        min_len -= 1
        max_len += 1

    if max_len < min_len:
        print(min_heapq[0])
    else:
        print(-max_heapq[0])