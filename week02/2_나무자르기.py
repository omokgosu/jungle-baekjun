
n , m = map(int , input().split(' '))

trees = sorted(list(map(int,input().split(' '))))

max_tree = trees[len(trees)-1]

def binary_search(left,mid,right):
    # m  내가 필요한 나무의 높이 (잘라진 뒤)
    max_height = 0;

    while left <= right:
        total = 0

        for i in trees:
            if i > mid:
                total += i - mid

        if total == m:
            return print(mid)
        elif total < m:
            max_height = min(mid,max_height)
            right = mid - 1
        else:
            max_height = max(mid,max_height)
            left = mid + 1           

        mid = (left + right) // 2

    return print(max_height)


binary_search(0, max_tree // 2 , max_tree)