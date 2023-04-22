'''
- 0은 양, 1은 늑대
- 양의 수가 늑대의 수보다 많은가?
- 부모 노드를 방문한 적이 있는가?
- 자식 노드를 처음 방문하는가?
    1. 양이 늑대보다 많으면 결과 배열에 저장을 한다.
    2. edge 배열을 돌면서 방문한 부모 노드와 방문하지 않은 자식 노드라면, 자식 노드에 방문처리를 한다.
    3. 자식 노드의 정보로 양 또는 늑대 수를 갱신하여 재귀호출한다.
    4. 자식 노드의 방문처리를 원상복구한다.
    5. 위 과정을 반복한다.
- 풀이 참고
'''

def solution(info, edges):
    n = len(info)
    answer = []
    visited = [0] * n # 노드의 방문 처리 리스트
    visited[0] = 1 # 루트 노드는 항상 방문
    
    def dfs(sheep, wolf):
        if sheep > wolf: # 양 개수가 늑대 개수보다 많다면
            answer.append(sheep)
        else:
            return

        for p, c in edges:
            # 자식 노드를 방문하려면, 항상 그 자식의 부모노드를 방문해야 하고
            # 해당 자식 노드는 방문한 적이 없어야 한다.
            if visited[p] and not visited[c]:
                visited[c] = 1 # 해당 자식 노드 방문 처리
                if info[c] == 0: # 양이라면
                    dfs(sheep + 1, wolf) # 양의 개수 + 1을 하고 재귀호출
                else: # 늑대라면
                    dfs(sheep, wolf + 1) # 늑대 개수 + 1을 하고 재귀호출
                visited[c] = 0 # 다음 조합을 위해, 원상복구
    
     # 루트 노드부터 시작 (루트 노드는 무조건 양)
    dfs(1, 0)
    return max(answer)