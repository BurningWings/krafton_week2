"""
[BFS - 너비 우선 탐색과 최단 거리]

문제 설명:
- BFS(Breadth-First Search)는 시작 정점에서 가까운 정점부터 탐색합니다.
- 큐(Queue)를 사용하며, 먼저 큐에 넣은 정점을 먼저 꺼냅니다.
- 가중치가 없는 그래프에서 BFS를 사용하면 시작 정점으로부터
  각 정점까지 가는 최소 간선 수를 구할 수 있습니다.

그래프 구조:

        3
        |
        1 --- 4
       /       \
      0         5
       \       /
        2 -----

입력:
- graph: 인접 리스트 형태의 그래프
- start: 탐색을 시작할 정점

출력:
- start에서 각 정점까지의 최단 거리가 담긴 딕셔너리
- start에서 갈 수 없는 정점은 결과에 포함하지 않습니다.
"""

from collections import deque


def bfs_distance(graph, start):
    """
    BFS로 시작 정점에서 각 정점까지의 최단 거리 구하기

    Args:
        graph: 인접 리스트 딕셔너리
        start: 시작 정점

    Returns:
        시작 정점에서 각 정점까지의 최단 거리가 담긴 딕셔너리
    """
    # TODO:
    # 1. 거리를 저장할 딕셔너리를 만드세요.
    #    시작 정점의 거리는 0입니다.
    #
    # 2. deque를 사용해 큐를 만드세요.
    #    시작 정점을 큐에 넣으세요.
    #
    # 3. 큐가 빌 때까지 반복하세요.
    #
    # 4. 큐의 앞에서 현재 정점을 꺼내세요.
    #
    # 5. 현재 정점과 연결된 이웃 정점을 하나씩 확인하세요.
    #
    # 6. 아직 거리가 기록되지 않은 정점이면:
    #    - 현재 정점 거리 + 1을 이웃 정점의 거리로 저장하세요.
    #    - 이웃 정점을 큐에 넣으세요.
    #
    # 7. 거리 딕셔너리를 반환하세요.
    pass


if __name__ == "__main__":
    graph = {
        0: [1, 2],
        1: [0, 3, 4],
        2: [0, 5],
        3: [1],
        4: [1, 5],
        5: [2, 4],
        6: []
    }

    print("=== BFS 최단 거리 ===")

    start = 0
    distances = bfs_distance(graph, start)

    print(f"시작 정점: {start}")

    for vertex in sorted(distances):
        print(f"{start} → {vertex}: {distances[vertex]}개 간선")