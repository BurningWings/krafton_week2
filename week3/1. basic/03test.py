"""
[그래프 - 인접 리스트 표현]

문제 설명:
- 무방향 그래프를 인접 리스트로 표현합니다.
- 인접 리스트는 각 정점에 연결된 정점들을 리스트로 저장하는 방식입니다.
- 무방향 그래프는 A와 B가 연결되면 A → B, B → A를 모두 저장해야 합니다.

정점:
- 0, 1, 2, 3, 4, 5

간선:
- (0, 1)
- (0, 2)
- (1, 3)
- (1, 4)
- (2, 5)
- (4, 5)

그래프 구조:

        3
        |
        1 --- 4
       /       \
      0         5
       \       /
        2 -----

입력:
- vertices: 정점 개수
- edges: 연결된 정점 쌍 목록
- directed: 방향 그래프 여부

출력:
- 인접 리스트 딕셔너리
"""


def create_graph(vertices, edges, directed=False):
    """
    인접 리스트 방식으로 그래프를 만드는 함수

    Args:
        vertices: 정점 개수
        edges: (출발 정점, 도착 정점) 튜플이 담긴 리스트
        directed: 방향 그래프인지 여부

    Returns:
        각 정점의 이웃 정점이 담긴 딕셔너리
    """
    # TODO:
    # 1. 0부터 vertices - 1까지 모든 정점을 키로 만들고,
    #    각 값은 빈 리스트로 초기화하세요.
    #
    # 예: vertices가 3이면
    # {0: [], 1: [], 2: []}
    #
    # 2. edges를 하나씩 꺼내 u, v에 넣으세요.
    #
    # 3. u의 이웃 리스트에 v를 추가하세요.
    #
    # 4. directed가 False인 무방향 그래프라면
    #    v의 이웃 리스트에도 u를 추가하세요.
    graph = {}
    for i in range(vertices):
        graph[i] =[]
    for u , v in edges:
        graph[u].append(v)
        if directed == False:
            graph[v].append(u)
    return graph


if __name__ == "__main__":
    vertices = 6
    edges = [
        (0, 1),
        (0, 2),
        (1, 3),
        (1, 4),
        (2, 5),
        (4, 5)
    ]

    print("=== 무방향 그래프 ===")
    graph = create_graph(vertices, edges, directed=False)

    for vertex, neighbors in graph.items():
        print(f"{vertex} → {neighbors}")

    print()

    print("=== 방향 그래프 ===")
    directed_graph = create_graph(vertices, edges, directed=True)

    for vertex, neighbors in directed_graph.items():
        print(f"{vertex} → {neighbors}")