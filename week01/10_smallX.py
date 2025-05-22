def solution():
    
    n,x = map( int , input().split(' ') )
    a = list( map( int , input().split(' ') ) )

    for i in a:
        if i < x: print(i , end=' ')

solution()

# 시간복잡도 O(n) 수열을 이루는 정수 n개가 주어질때 n이 늘어날수록 비교연산이 늘어나므로 O(n) 으로 책정했다.
# 공간복잡도 O(n) 수열을 이루는 정수 n 개가 주어질 때, 리스트의 길이도 늘어나므로 O(n) 으로 책정했다.