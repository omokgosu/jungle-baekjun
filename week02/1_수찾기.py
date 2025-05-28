

# 문제에 이분탐색 이라고 되어있는 만큼 이분탐색을 사용해보기로 했어.
# if 'apple' in fruits:  같은 메소드는 시간복잡도 O(n) 을 가짐.
# 이분 탐색을 사용할 경우 시간복잡도 O(log n) 을 가짐.
# 이 문제 같은 경우는 배열에서 검색을 여러번 해야하기 때문에 in 메소드를 사용하기보다 정렬을 한번하고 이분탐색을 사용해보자!
# python 의 sort 를 사용하면 n log n 복잡도로 정렬을 한번하고 log n 으로 여러번 검색하자잉!

n = int(input())

array = sorted(list(input().split(' ')))

m = int(input())

target_array = list(input().split(' '))

for i in range(m):
    target = target_array[i]

    def Binary_search(left,mid,right):

        while left <= right:
            if array[mid] == target: 
                return print(1)
            elif array[mid] <= target:
                left = mid + 1
            else: 
                right = mid - 1

            mid = (left + right)//2

        return print(0)

    Binary_search( 0, len(array)//2 , len(array)-1 )


