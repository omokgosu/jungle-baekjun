import sys
input = lambda: sys.stdin.readline().strip()


# 입력받은 문자열
string = input().split('-')

for i in range(len(string)):
    if '+' in string[i]:
        total = sum(list(map(int,string[i].split('+'))))
        string[i] = total

result = int(string[0])
for j in range(1 , len(string)):
    result -= int(string[j])

print(result)