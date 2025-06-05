import sys

# 재귀호출 범위 늘리기
sys.setrecursionlimit(10 ** 9)

tree = list(map(int,sys.stdin.read().splitlines()))

def postOrder(start,end):
    if start > end:
        return

    mid = end + 1
    for i in range(start + 1 , end + 1):
        # start 보다 큰 게 있다 = 트리의 오른쪽이 있다.
        if tree[i] > tree[start]:
            # 그 트리를 루트로 해준다.
            mid = i
            break;

    # 왼쪽트리 타기
    postOrder(start + 1 , mid - 1)
    postOrder(mid, end)
    print(tree[start])

postOrder(0, len(tree) - 1)