"""
[이진 검색 트리 - BST 값 검색]

문제 설명:
- 이진 검색 트리(Binary Search Tree, BST)에서 특정 값을 찾습니다.
- BST는 현재 노드보다 작은 값은 왼쪽, 큰 값은 오른쪽에 저장됩니다.
- 이 규칙을 사용하면 모든 노드를 확인하지 않고 한쪽 방향만 탐색할 수 있습니다.

트리 구조:

        12
       /  \
      7    18
     / \   / \
    4   9 15  22

입력:
- root: BST의 루트 노드
- target: 찾을 값

출력:
- target이 트리에 있으면 True
- 없으면 False
"""


class TreeNode:
    """BST 노드"""

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def search_bst(root, target):
    """
    BST에서 target을 찾는 함수

    Args:
        root: 현재 확인할 노드
        target: 찾을 값

    Returns:
        target이 있으면 True, 없으면 False
    """
    # TODO:
    # 1. root가 None이면 False를 반환하세요.
    # 2. 현재 노드 값이 target과 같으면 True를 반환하세요.
    # 3. target이 현재 노드 값보다 작으면 왼쪽을 재귀 호출하세요.
    # 4. target이 현재 노드 값보다 크면 오른쪽을 재귀 호출하세요.
    if root == None:
        return False

    if root.value == target:
        return True
    if target < root.value:
        return search_bst(root.left,target)
    if target > root.value:
        return search_bst(root.right,target)


if __name__ == "__main__":
    # 아래 BST를 직접 만드세요.
    #
    #         12
    #        /  \
    #       7    18
    #      / \   / \
    #     4   9 15  22

    root = TreeNode(12)
    root.right = TreeNode(18)
    root.left = TreeNode(7)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(9)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(22)

    # TODO: 7, 18, 4, 9, 15, 22 노드를 연결하세요.

    print("=== BST 검색 ===")

    targets = [4, 9, 12, 15, 22, 10, 30]

    for target in targets:
        result = search_bst(root, target)
        print(f"{target} 검색 결과: {result}")