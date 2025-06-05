import sys
input = sys.stdin.readline

# treeNode 클래스 생성
class treeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

# 전위순회 
def preorder(node):
    if node:
        print(node.val , end='')
        preorder(node.left)
        preorder(node.right)

# 중위순회
def inorder(node):
    if node:
        inorder(node.left)
        print(node.val , end='')
        inorder(node.right)

# 후위순회
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.val , end='')

# 총 입력 갯수
n = int(input())
nodes = {}

for i in range(n):
    parent, left, right = input().strip().split(' ')
    
    # 노드 없으면 생성
    if parent not in nodes:
        nodes[parent] = treeNode(parent)
    if left != '.' and left not in nodes:
        nodes[left] = treeNode(left)
    if right != '.' and right not in nodes:
        nodes[right] = treeNode(right)

    # 자식연결
    nodes[parent].left = nodes.get(left) if left != '.' else None
    nodes[parent].right = nodes.get(right) if right != '.' else None

# 루트는 A로 고정
root = nodes['A']

# print(nodes)

preorder(root)
print('')
inorder(root)
print('')
postorder(root)