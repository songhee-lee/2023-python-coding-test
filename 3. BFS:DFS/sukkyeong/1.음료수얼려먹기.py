from collections import deque

# bfs 함수 정의


def bfs(x, y, ice_frame):
    # 너비 우선 탐색을 위한 큐 생성
    queue = deque()
    # 현재 위치를 큐에 삽입하고 방문 처리
    queue.append((x, y))
    ice_frame[x][y] = 1
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        x, y = queue.popleft()
        # 현재 위치에서 네 방향으로의 위치 확인
        if x > 0 and ice_frame[x-1][y] == 0:
            queue.append((x-1, y))
            ice_frame[x-1][y] = 1
        if x < len(ice_frame)-1 and ice_frame[x+1][y] == 0:
            queue.append((x+1, y))
            ice_frame[x+1][y] = 1
        if y > 0 and ice_frame[x][y-1] == 0:
            queue.append((x, y-1))
            ice_frame[x][y-1] = 1
        if y < len(ice_frame[0])-1 and ice_frame[x][y+1] == 0:
            queue.append((x, y+1))
            ice_frame[x][y+1] = 1


# 입력 받기
n, m = map(int, input().split())
ice_frame = []
for i in range(n):
    ice_frame.append(list(map(int, input())))

# 아이스크림 개수 카운트 변수 초기화
ice_count = 0

# 모든 위치에서 너비 우선 탐색 실행
for i in range(n):
    for j in range(m):
        # 현재 위치에서 너비 우선 탐색 실행
        if ice_frame[i][j] == 0:
            bfs(i, j, ice_frame)
            # 한 번의 너비 우선 탐색으로 하나의 아이스크림이 만들어지므로 ice_count 증가
            ice_count += 1

# 결과 출력
print(ice_count)
