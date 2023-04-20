'''
각 온라인 강의는 선수 강의가 있을 수 있음
선수강의가 있으면 먼저 듣고 해당 강의 수강 가능
n개의 강의가 있고, 1~n번의 번호, 동시에 여러 개 수강 가능
n개의 강의에 대해 수강하기까지 걸리는 최소 시간을 출력
'''

# 필요한 모듈 불러오기
from collections import deque

# 노드의 개수 입력받기
n = int(input())

# 모든 노드에 대한 진입 차수는 0으로 초기화
in_degree = [0] * (n + 1)

# 각 노드에 연결된 간선 정보를 담기 위한 인접 리스트 초기화
adj_list = [[] for _ in range(n + 1)]

# 각 강의 시간을 0으로 초기화
lecture_time = [0] * (n + 1)

# 방향 그래프의 모든 간선 정보를 입력받기
for i in range(1, n + 1):
    data = list(map(int, input().split()))
    lecture_time[i] = data[0]  # 첫 번째 수는 시간 정보를 담고 있음
    for x in data[1:-1]:
        in_degree[i] += 1
        adj_list[x].append(i)

# 위상 정렬 함수
def topology_sort():
    # 알고리즘 수행 결과를 담을 리스트
    min_time = [0] * (n + 1)

    # 큐 기능을 위한 리스트 사용
    q = []

    # 처음 시작할 때는 진입 차수가 0인 노드를 큐에 삽입
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.pop(0)
        # 해당 원소와 연
