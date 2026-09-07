"""
[이진 트리 - 순회]

문제 설명:
- 이진 트리를 만들고 전위·중위·후위 순회 결과를 리스트로 반환합니다.
- 각 순회 방식의 방문 순서를 이해하는 문제입니다.

트리 구조:

        10
       /  \
      6    15
     / \     \
    3   8     20

입력:
- root: 이진 트리의 루트 노드

출력:
- 전위 순회: 루트 → 왼쪽 → 오른쪽
- 중위 순회: 왼쪽 → 루트 → 오른쪽
- 후위 순회: 왼쪽 → 오른쪽 → 루트
"""


class TreeNode:
    """이진 트리 노드"""

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def preorder(root):
    """
    전위 순회 함수

    Args:
        root: 현재 방문할 노드

    Returns:
        전위 순회 결과 리스트
    """
    # TODO:
    # 1. root가 None이면 빈 리스트를 반환하세요.
    # 2. 현재 노드 값을 결과에 추가하세요.
    # 3. 왼쪽 서브트리를 순회하세요.
    # 4. 오른쪽 서브트리를 순회하세요.
    if root == None:
        return []
    a = []
    a.append(root.value)
    a.extend(preorder(root.left))
    a.extend(preorder(root.right))
    return a

def inorder(root):
    """
    중위 순회 함수

    Args:
        root: 현재 방문할 노드

    Returns:
        중위 순회 결과 리스트
    """
    # TODO:
    # 1. root가 None이면 빈 리스트를 반환하세요.
    # 2. 왼쪽 서브트리를 먼저 순회하세요.
    # 3. 현재 노드 값을 결과에 추가하세요.
    # 4. 오른쪽 서브트리를 순회하세요.
    if root == None:
        return []
    a = []
    
    a.extend(inorder(root.left))
    a.append(root.value)
    a.extend(inorder(root.right))
    return a

def postorder(root):
    """
    후위 순회 함수

    Args:
        root: 현재 방문할 노드

    Returns:
        후위 순회 결과 리스트
    """
    # TODO:
    # 1. root가 None이면 빈 리스트를 반환하세요.
    # 2. 왼쪽 서브트리를 먼저 순회하세요.
    # 3. 오른쪽 서브트리를 순회하세요.
    # 4. 마지막에 현재 노드 값을 결과에 추가하세요.
    if root == None:
        return []
    a = []
   
    a.extend(postorder(root.left))
    a.extend(postorder(root.right))
    a.append(root.value)
    return a
if __name__ == "__main__":
    # 아래 트리 구조를 직접 만드세요.
    #
    #         10
    #        /  \
    #       6    15
    #      / \     \
    #     3   8     20

    root = TreeNode(10)
    root.left = TreeNode(6)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(8)
    root.right = TreeNode(15)
    root.right.right = TreeNode(20)
    # TODO: 6, 15, 3, 8, 20 노드를 연결하세요.

    print("=== 이진 트리 순회 ===")
    print(f"전위 순회: {preorder(root)}")
    print(f"중위 순회: {inorder(root)}")
    print(f"후위 순회: {postorder(root)}")