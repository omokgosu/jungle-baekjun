def solution():

    array = []

    for i in range(9):
        array.append(int(input()))

    num = max(array)
    position = array.index(num)

    print(f'{num} {position+1}')

solution()

# 시간복잡도  O(1) 최댓값찾기 O(n) + index 찾기 O(n) 해서 O(n) 으로 생각할 수 있지만 9로 크기가 고정되어있기 때문에 O(1) 의 상수복잡도를 가진다.
# 공간복잡도 O(1) 마찬가지로 n 값이 고정되어있기 때문에 O(1) 의 상수 복잡도를 가진다.