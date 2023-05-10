from collections import deque

for _ in range(int(input())):   # 테스트 케이스 반복
    N = int(input())        # 팀의 수
    indegree = [0] * (N+1)  # 진입 차수
    graph = [[False]*(N+1) for _ in range(N+1)] # 방향 그래프

    # 작년 순위 입력받기
    data = list(map(int, input().split()))
    for i in range(N):
        for j in range(i+1, N):
            graph[data[i]][data[j]] = True  # i -> j  낮은 팀 가리키기
            indegree[data[j]] += 1          # 낮은 팀 진입차수 +1

    M = int(input())        # 바뀐 순위 정보 개수
    for _ in range(M):
        a, b = map(int, input().split())    # a가 b보다 낮았는데 높아졌다

        # 간선 방향 뒤집기
        # 현재 a가 b보다 높은 경우
        if graph[a][b] :
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        # 현재 a가 b보다 낮은 경우
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1
    
    # 위상 정렬
    result = []     # 순위 리스트
    q = deque() 

    # 진입 차수 0인 노드 큐에 삽입
    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)
    
    only_one = True     # 경우의 수가 하나인 경우
    cycle = False       # 사이클이 존재하는 경우

    for i in range(N):
        if len(q) == 0 :    # N번 반복 전에 큐가 비었다!
            cycle = True    # 사이클이 존재한다.
            break
    
        if len(q) >= 2:      # 큐에 2개 이상의 노드가 있다!
            only_one = False # 여러 개 경우의 수가 존재한다.
            break
        
        # 현재 노드와 연결된 노드들 진입차수 -1 
        now = q.popleft()
        result.append(now)
        for j in range(1, N+1):
            if graph[now][j] :
                indegree[j] -= 1

                if indegree[j] == 0:    # 새로 진입차수 0이 되는 노드 삽입
                    q.append(j)
    
    if cycle:
        print("IMPOSSIBLE")
    elif not only_one:
        print("?")
    else:
        print(*result)
