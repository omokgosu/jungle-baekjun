import sys
input = sys.stdin.readline

# 비트
A_str = input().strip()
B_str = input().strip()

# 입력 문자열의 길이 저장
bit_length = len(A_str)

# 이진수 문자열을 정수로 변환
A = int(A_str, 2)
B = int(B_str, 2)

# 원래 비트 길이만큼 출력
print(f'{A & B:0{bit_length}b}')
print(f'{A | B:0{bit_length}b}')
print(f'{A ^ B:0{bit_length}b}')
print(f'{~A & ((1 << bit_length) - 1):0{bit_length}b}')
print(f'{~B & ((1 << bit_length) - 1):0{bit_length}b}')