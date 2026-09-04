"""
[DFS - 깊이 우선 탐색 (Depth-First Search)]

문제 설명:
- DFS로 그래프를 탐색합니다.
- 깊이 방향으로 끝까지 탐색합니다.
- 재귀 또는 스택을 사용합니다.

입력:
- graph: 그래프 (인접 리스트)
- start: 시작 정점

출력:
- 방문 순서

예제:
그래프:
  0 ─── 1
  │     │
  └─ 2 ─┘
      │
      3

시작: 0
DFS: [0, 1, 2, 3] (순서는 구현에 따라 다를 수 있음)

힌트:
- 재귀로 구현
- 방문 체크 필요
- 깊이 우선으로 방문
"""
def dfs(graph, start, visited=None):
    """
    깊이 우선 탐색 (재귀)
    
    Args:
        graph: 그래프 
        start: 현재 
        visited: 방문 
    
    Returns:W
        방문 순서 
    """
    # TODO: visited가 None이면 
    if visited is None:
        visited = set()
    
    # TODO: 현재 정점 
    
    if start in visited:
        return
    if start not in visited:
        visited.add(start)
        for i in graph[start]:
            if i not in visited:
                dfs(graph,i,visited)
                
    
    # TODO: 인접한 정점들에 대해 
    ## 방문하지 않은 정점이면 재귀 
    
    
    return list(visited)

# 테스트 
if __name__ == "__main__":
    # 그래프 
    graph = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1, 3],
        3: [2]  
    }
    
    print("=== DFS (깊이 우선 탐색) ===")
    result = dfs(graph, 0)
    print(f"시작 정점: 0")
    print(f"방문 순서: {result}")


