from collections import deque

N = int(input())
graph = [[] for _ in range(N+1)]
time = [0] * (N+1)
indegree = [0] * (N+1)      # 진입 차수

for i in range(1, N+1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for pre in data[1:-1]:    # 각 선수과목에 대해
        indegree[i] += 1        # 진입차수 +1
        graph[pre].append(i)    # 그래프 연결

result = time[:]        # 결과 담을 리스트
q = deque()

# 진입 차수가 0인 노드 삽입
for i in range(1, N+1):
    if indegree[i] == 0 :
        q.append(i)

# 큐가 빌 때까지 반복
while q:
    now = q.popleft()

    for i in graph[now]:
        # 현재 강의 수강하는데 필요한 시간 VS 선수과목 + 현재 강의 시간
        result[i] = max(result[i], result[now]+time[i])
        indegree[i] -= 1

        if indegree[i] == 0:
            q.append(i)

for i in range(1, N+1):
    print(result[i])