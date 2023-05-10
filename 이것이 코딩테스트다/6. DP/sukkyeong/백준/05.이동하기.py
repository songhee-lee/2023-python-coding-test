

'''
N, M을 입력받아서 배열 maze와 dp를 생성합니다.
dp 배열을 초기화합니다. dp[0][0]은 시작 위치의 값으로 초기화합니다.
첫 행과 첫 열의 값을 초기화합니다. 첫 행은 왼쪽의 값과 현재 값의 합으로, 첫 열은 위쪽의 값과 현재 값의 합으로 초기화합니다.
dp 배열의 나머지 부분을 채웁니다. 현재 위치의 dp 값은 왼쪽 값, 위쪽 값, 대각선 위의 값 중 최대값에 현재 위치의 값을 더한 값입니다.
dp[N-1][M-1]을 출력합니다. 이 값은 오른쪽 아래의 값이 됩니다.

'''
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

# 배열 생성 및 초기화
maze = []
for i in range(N):
    row = list(map(int, input().split()))
    maze.append(row)

# dp 배열 생성 및 초기화
dp = [[0] * M for _ in range(N)]
dp[0][0] = maze[0][0]  # 시작 위치 초기화

# 첫 행 초기화
for j in range(1, M):
    dp[0][j] = dp[0][j-1] + maze[0][j]

# 첫 열 초기화
for i in range(1, N):
    dp[i][0] = dp[i-1][0] + maze[i][0]

# dp 배열 채우기
for i in range(1, N):
    for j in range(1, M):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + maze[i][j]

# 결과 출력
print(dp[N-1][M-1])
