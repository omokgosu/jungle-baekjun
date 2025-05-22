from itertools import permutations

def solution():
    
    n = int(input())
    arr = [ list(map(int,input().split(' '))) for i in range(n) ]

    city = [ int(i) for i in range(n) ]

    permutation = list(permutations(city,n))


    minValue = float("inf")

    for i in permutation:
        total = 0
        check = False
        n = len(i)
        
        for j in range(n):
            start = j
            end = j+1         
            
            if end > n-1: end = 0

            if arr[i[start]][i[end]] == 0: 
                check = True
                break

            total += arr[i[start]][i[end]]
            
        if check: continue
        
        minValue = min(minValue , total)

    print(minValue)
    
solution()