import queue

n, m = map(int, input().split())
s = []
queue = []
# 너비 우선 탐색
# 이동할 방향 선택(상, 하, 좌, 우)
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    s.append(list(input()))
queue = [[0, 0]]
s[0][0] = 1

while queue:
    a, b = queue[0][0], queue[0][1]
    del queue[0]
    # 현재 위치에서 4가지 방향으로 위치 확인
    for i in range(4):
        x = a + dx[i]
        y = b + dy[i]
        # 동서남북을 검사해서 '1'인 경우의 수를 찾는다
        if 0 <= x < n and 0 <= y < m and s[x][y] == '1':
            queue.append([x, y])
            s[x][y] = s[a][b] + 1
# 최솟값을 리턴
print(s[n-1][m-1])
