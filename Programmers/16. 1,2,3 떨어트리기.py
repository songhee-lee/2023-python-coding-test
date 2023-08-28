# .ref
# 단방향
# 앞서 떨어트린 숫자가 리프 노드까지 떨어진 후에 새로운 숫자를 떨어트려야 한다.
# 숫자가 지나간 각 노드는 현재 길로 연결된 자식 노드 다음으로 번호가 큰 자식 노드를 가리키는 간선을 새로운 길로 설정
import math

def solution(edges, target):
    max_node_num = len(target) + 1  # 노드 번호 최댓값
    
    # 1. 트리 구성하기
    tree = {i: [] for i in range(1, max_node_num)}
    for edge in edges:
        parent, child = edge
        tree[parent].append(child)
        
    # 2. 리프노드 설정 & 자식 노드 중 가장 번호가 작은 노드를 가리키는 간선을 초기 길로 설정
    leaf_count = {} # 리프노드에 몇 개의 숫자가 떨어졌는지 저장
    for t in tree:
        if tree[t]:
            tree[t] = sorted(tree[t]) 
        else:
            leaf_count[t] = 0
            
    # 3. 자식 노드 중 가장 번호가 작은 노드를 가리키는 간선을 초기 길로 설정하기
    child_path = [-1] * (max_node_num) # 각 노드의 길로 설정된 자식 노드
    for i in range(1, len(tree)):
        if tree[i]:
            child_path[i] = 0 # ➡️ 부모노드(i)의 초기 길로 설정된 자식의 인덱스 = 0
            
    # 4. 리프노드 방문횟수 구하기
    order = [] # 방문한 리프노드의 순서
    _exit = False # 리프노드들을 계속 방문해도 되는지
    while not _exit:
        root_node = 1 # 초기에 1번 노드에서 숫자를 떨어트린다.
        
        # 4.1 길 재설정하기
        while child_path[root_node] != -1: # 리프 노드가 아닐 때 까지
            cur_node = root_node
            root_node = tree[root_node][child_path[root_node]] # 현재 길
            if len(tree[cur_node]) > child_path[cur_node] + 1: # 길 재설정
                child_path[cur_node] += 1
            else: # 부모가 가지고 있는 자식 노드들의 크기를 넘긴다면, 다시 맨 왼쪽 자식을 길로 설정한다.(=현재 길로 연결된 노드의 번호가 가장 크면, 번호가 가장 작은 노드를 가리키는 간선을 길로 설정한다.)
                child_path[cur_node] = 0
        
        # 이 시점에서, root_node는 리프노드를 의미하게 된다.
        order.append(root_node) # 방문한 리프노드 순서 저장
        leaf_count[root_node] += 1 # 리프 노드에 떨어진 숫자 개수 증가
        
        # 4.2 리프노드의 방문횟수 확인
        _exit = True
        for leaf in leaf_count:
            # e.g. target이 5일 경우, 1이 5번 들어가는게 최대 방문횟수이고 3이 2번 들어가는게 최소 방문횟수이다. ➡️ 2 ~ 5번까지 방문이 가능하다.
            # 이때 리프노드를 6번 방문했다면 최솟값인 1로도 5를 만들 수 없으므로 실패이다.
            if leaf_count[leaf] < int(math.ceil(target[leaf - 1] / 3)): # 리프노드에 숫자가 더 떨어져도 되는 경우(=리프노드를 더 방문해도 되는 경우)
                _exit = False
                break
            elif leaf_count[leaf] > target[leaf - 1]: # 실패 조건
                return [-1]

    # 5. 실제 숫자 떨어트리기
    
    # 사전 순으로 가장 빠른 경우를 찾아야 하므로, 1을 먼저 배치해야 한다.
    answer = [1 for _ in range(len(order))]
    for leaf in order:
        target[leaf - 1] -= 1 # 숫자 1을 모든 방문한 리프노드에 떨어트린다.
    
    # 1을 미리 채웠으니, 2, 1, 0를 떨어트린다.
    # 사전 순으로 가장 빠른 경우를 찾아야 하므로, 방문한 리프노드들 중 맨 뒤부터 큰 숫자를 떨어트린다.
    for i in range(len(order) - 1, -1, -1):
        if target[order[i] - 1] >= 2: # 2 떨어트리기
            answer[i] += 2
            target[order[i] - 1] -= 2
        elif target[order[i] - 1] == 1: # 1 떨어트리기
            answer[i] += 1
            target[order[i] - 1] -= 1
        else: # target[order[i] - 1] == 0 ➡️ 0 떨어트리기(변화 없음)
            continue
        
    return answer