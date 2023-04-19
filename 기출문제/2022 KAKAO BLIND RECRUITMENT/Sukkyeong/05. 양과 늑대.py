'''
양을 최대한 많이 모으기
늑대가 따라오는데 양보다 많아지면 양 0마리 됨
1 1 x x 1-> 1마리 됨
1 x 1  -> 2마리 됨

예를 들어, 위 그림의 경우(루트 노드에는 항상 양이 있습니다) 0번 노드(루트 노드)에서 출발하면 양을 한마리 모을 수 있습니다. 다음으로 1번 노드로 이동하면 당신이 모은 양은 두 마리가 됩니다. 이때, 바로 4번 노드로 이동하면 늑대 한 마리가 당신을 따라오게 됩니다. 아직은 양 2마리, 늑대 1마리로 양이 잡아먹히지 않지만, 이후에 갈 수 있는 아직 방문하지 않은 모든 노드(2, 3, 6, 8번)에는 늑대가 있습니다. 이어서 늑대가 있는 노드로 이동한다면(예를 들어 바로 6번 노드로 이동한다면) 양 2마리, 늑대 2마리가 되어 양이 모두 잡아먹힙니다. 여기서는 0번, 1번 노드를 방문하여 양을 2마리 모은 후, 8번 노드로 이동한 후(양 2마리 늑대 1마리) 이어서 7번, 9번 노드를 방문하면 양 4마리 늑대 1마리가 됩니다. 이제 4번, 6번 노드로 이동하면 양 4마리, 늑대 3마리가 되며, 이제 5번 노드로 이동할 수 있게 됩니다. 따라서 양을 최대 5마리 모을 수 있습니다.

0은 양
1은 늑대
[부모노드 번호, 자식노드번호]
모은 양의 개수를 cnt += 1로함

'''
def dfs(idx, sheep, wolf, possible):
    global g_info, answer, graph

    # 현재 위치에 양이 있다면 sheep 변수를 1 증가
    if g_info[idx] == 0:
        sheep += 1
        answer = max(answer, sheep)
    else: # 현재 위치에 늑대가 있다면 wolf 변수를 1 증가
        wolf += 1

    # 만약 늑대의 수가 양의 수보다 많다면 불가능한 경우이므로 종료
    if wolf >= sheep:
        return

    # 현재 위치에서 갈 수 있는 위치들을 possible 리스트에 추가
    possible.extend(graph[idx])

    # possible 리스트에 있는 위치들을 dfs 탐색
    for p in possible:
        dfs(p, sheep, wolf, [i for i in possible if i != p])

def solution(info, edges):
    global answer, g_info, visited, graph
    answer = 0
    g_info = info
    n = len(info)
    graph = [[] for _ in range(n)]

    # 그래프를 만들어주는 과정
    for a, b in edges:
        graph[a].append(b)

    # dfs 탐색 시작
    dfs(0, 0, 0, [])
    return answer
