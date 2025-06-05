import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

# 부모 찾기
def find(parent,x):
    # 루트를 찾을 때 까지 ( 부모가 자기 자신일 때 까지 )
    if parent[x] != x:
        # 자신의 부모의 루트를 찾고, 결과를 저장
        parent[x] = find(parent,parent[x])
    
    return parent[x]

# 합치기
def union(parent,a,b):
    # 두 원소의 루트찾기
    a = find(parent, a)
    b = find(parent, b)

    # 한쪽 루트를 다른 쪽 부모의 루트로 설정
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# N 은 정점의 개수
# N 은 간선의 개수
N,M = map(int,input().split(' '))

graph = []
parent = [ i for i in range(N+1)]

for i in range(M):
    # u는 정점
    # v 는 도착점
    # c 는 간선 ( 음수일수도있음 )
    u,v,w = map(int, input().strip().split(' '))
    graph.append((u,v,w))

# 최소 스패닝 트리를 저장할 트리배열
graph.sort(key = lambda x: x[2], reverse=True)

# 연결된 간선 갯수 n-1개까지
count = 0
# 최소 거리 덧셈
result = 0

# 간선의 길이가 N-1 이 될 때까지
while count < N-1:
    # 간선의 길이가 가장짧은 노드를 pop
    u,v,w = graph.pop()

    # 루트노드 찾기
    a = find(parent,u)
    b = find(parent,v)

    # 루트노드가 같으면 사이클 발생임
    if a == b: continue

    # 다르면 추가
    count += 1
    result += w

    union(parent,u,v)

    print(result,parent)


print(result)