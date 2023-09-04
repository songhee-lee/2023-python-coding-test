"""
- 좌표가 주어졌을 때 전위 순회와 후위 순회의 결과 리턴하기
- 자식 노드의 y값은 항상 부모 노드보다 작다.
- V노드의 왼쪽 서브트리의 x값은 항상 V의 x값보다 작고 오른쪽 서브트리는 크다.

- 1 <= 노드 개수 <= 10,000
- 1 <= 트리 깊이 <= 1000

"""

import sys
sys.setrecursionlimit(10**4)

# 루트 찾기
def find_root(coord_x) :
    rx, ry, ri, x_idx = 0, 0, 0, 0
    for idx, (x, y, i) in enumerate(coord_x) :
        if y >= ry :
            rx, ry, ri, x_idx = x, y, i, idx
    return rx, ry, ri, x_idx

# 트리 순회하기
# 전위 순회 : 루트 - 왼쪽 - 오른쪽
# 후위 순회 : 오른쪽 - 왼쪽 - 루트
def treeorder(coord_x, order, how="pre") :
    
    rx, ry, ri, x_idx = find_root(coord_x)	# 루트 찾기
    
    
    if how == "pre" :           # 루트 (전위 순회)
        order += [ri]			
    
    if x_idx > 0 :              # 왼쪽 자식
        order += treeorder(coord_x[:x_idx], [], how)
    
    if x_idx < len(coord_x)-1 : # 오른쪽 자식
        order += treeorder(coord_x[x_idx+1:], [], how)
    
    if how == "post" :          # 루트 (후위 순회)
        order += [ri]
        
    return order

    
def solution(nodeinfo):
    n = len(nodeinfo)       # 노드 개수
    nodeinfo = [(x, y, i+1) for i, (x, y) in enumerate(nodeinfo) ]   # (x좌표, y좌표, 노드 번호)
    coord_x = sorted(nodeinfo, key=lambda x: x[0])      # x좌표 정렬
    
    return [treeorder(coord_x, [], "pre"), treeorder(coord_x, [], "post")]