#################################Binary Tree
# class Node:
#     def __init__(self, data):
#         self.data = data;
#         self.left = None;
#         self.right = None;
#
# class bTree:
#     def __init__(self):
#         self.root = None;
#     def inorderTraverse(self, root):
#         if root is None:
#             return;
#         self.inorderTraverse(root.left);
#         print(root.data, end='\n');
#         self.inorderTraverse(root.right);
#
# def makeSubNode(root, newNode):
#     if root.data > newNode.data:
#         makeLeftNode(root, newNode);
#     else:
#         makeRightNode(root, newNode);
#
# def makeRightNode(root, newNode):
#     if root.right is None:
#         root.right = newNode;
#     else:
#         makeSubNode(root.right, newNode);
#
# def makeLeftNode(root, newNode):
#     if root.left is None:
#         root.left = newNode;
#     else:
#         makeSubNode(root.left, newNode);
#
# N = int(input());
#
# tree = bTree();
# for i in range(N):
#     newNode = Node(int(input()));
#     if tree.root is None:
#         tree.root = newNode;
#     else:
#         makeSubNode(tree.root, newNode);
#
# tree.inorderTraverse(tree.root);


#################################버블정렬
# N = int(input());
# arr = [];
#
# for i in range(N):
#         arr.append((int(input())));
#
#
# for i in range(N-1):
#     for j in range(N-1-i):
#         if arr[j]>arr[j+1]:
#             temp = arr[j];
#             arr[j] = arr[j+1];
#             arr[j+1] = temp;
#
# for n in arr:
#     print(n);


N = int(input());
arr = [];

for i in range(N):
        arr.append((int(input())));

def quickSort(arr, start, end):# 재귀함수용 함수 선언(리스트, 시작인덱스, 종료인덱스)
    if start < end: # 시작 인덱스 보다 끝 인덱스가 클 경우
        left = start # left 변수에 시작 인덱스 할당
        pivot = arr[end] #  //pivot 값은 a리스트에 마지막 원소 값
        for i in range(start, end): # 시작인덱스부터 끝 원소까지 반복
            if arr[i] < pivot: # 리스트 인덱스 값이 pivot 값보다 작을 경우라면
                arr[i], arr[left] = arr[left], arr[i] #  해당 인덱스와 left인덱스  swap
                left += 1 # 인덱스 하나 증가 시켜주기(자리를 옮겨가며 비교해야 하기 때문에)
        arr[left] , arr[end] = arr[end], arr[left] # left인덱스와 끝 인덱스 swap
        quickSort(arr, start, left-1) # 재귀 호출 (리스트, 시작 인덱스, left-1)
        quickSort(arr, left+1, end) # 재귀 호출 (리스트, left+1, 종료인덱스)
quickSort(arr, 0, len(arr)-1)
for n in arr:
    print(n);