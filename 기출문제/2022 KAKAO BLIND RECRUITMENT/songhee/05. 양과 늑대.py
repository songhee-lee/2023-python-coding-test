"""
- 양을 모아서 루트 노드로 돌아오기
"""
from collections import deque

def solution(info, edges):
    child = [[] for _ in range(len(info))]  # 자식 노드
    parent = [0]*len(info)                  # 부모 노드
    for s, e in edges:
        child[s].append(e)  
        parent[e] = s
    
    # 루트 노드에서 양 한마리로 시작
    info[0] = -1
    q = deque([(0, 1, 0, info)])        #(위치, 양, 늑대 개수)
    visited = set()
    visited.add(tuple([0]+info))        #(위치 + info)
    answer = 0
    
    while q:
        loc, sheep, wolf, infos = q.popleft()
        answer = max(answer, sheep) # 최대 양 확인
        
        print(loc, sheep, wolf, infos)
        # 현재와 이어진 경로들 모두 확인하기
        for nxt in child[loc]:
            # 양인 경우
            if infos[nxt] == 0 and wolf < sheep+1 :
                infos[nxt] = -1
                q.append((nxt, sheep+1, wolf, infos[:]))
                visited.add(tuple( [nxt]+infos[:] ))
                infos[nxt] = 0
                
            # 늑대인 경우
            elif infos[nxt] == 1 and wolf+1 < sheep:
                infos[nxt] = -1
                q.append((nxt, sheep, wolf+1, infos[:]))
                visited.add(tuple( [nxt]+infos[:] ))
                infos[nxt] = 1

            # child를 이미 확인한 경우
            elif infos[nxt] == -1 and tuple([nxt]+infos) not in visited:
                q.append((nxt, sheep, wolf, infos[:]))
                visited.add(tuple([nxt]+infos[:]))
                
        # 부모 노드로의 이동
        if tuple([parent[loc]]+infos) not in visited:
            q.append((parent[loc], sheep, wolf, infos[:]))
            visited.add(tuple( [parent[loc]]+infos[:] )) 
    return answer