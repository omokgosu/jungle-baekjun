import sys
input = sys.stdin.readline

# N은 멀티탭 구멍의 갯수
# K는 전기용품 사용 횟수
N,K = map(int, input().split())

# 멀티탭
multi_tap = [ ]

# 스케쥴
schedule = list(map(int,input().split()))

# 교체횟수
count = 0

# 스케쥴링
for i in range(len(schedule)):
    current = schedule[i]

    # 이미 멀티탭에 있으면 패스
    if current in multi_tap:
        continue

    # 멀티탭에 자리 있으면 교체하지않고 걍 넣음
    if len(multi_tap) < N:
        multi_tap.append(current)
        continue

    # 아니면 교체인데..
    # 가장 나중에 나오는 놈을 교체?
    rest_schedule = schedule[i:]
    check_multi_tap = []
    remove_multi_tap_item = -1

    for j in multi_tap:
        if j in rest_schedule:
            check_multi_tap.append(rest_schedule.index(j))
        else:
            remove_multi_tap_item = j
            break

    if remove_multi_tap_item == -1:
        remove_multi_tap_item = multi_tap[check_multi_tap.index(max(check_multi_tap))]
    

    multi_tap.remove(remove_multi_tap_item)
    multi_tap.append(current)
    count += 1

print(count)
