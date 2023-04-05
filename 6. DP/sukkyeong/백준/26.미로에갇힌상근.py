import sys

dx = [-2, -1, 1, 2, 1, -1]  # 이동할 수 있는 방향의 x좌표 변화량
dy = [0, 1, 1, 0, -1, -1]  # 이동할 수 있는 방향의 y좌표 변화량


def f(x, y, count):
    # 이동 가능한 수(count)가 0이면 현재 위치가 시작점인지 확인 후, 1 또는 0을 반환합니다.
    if count == 0:
        if x == 0 and y == 0:
            return 1
        else:
            return 0

    # 현재 위치에서 이동 가능한 위치의 개수를 찾기 위한 동적 계획법을 수행합니다.
    if dp[x][y][count] == -1:
        res = 0
        for k in range(6):
            nx, ny = x + dx[k], y + dy[k]
            if inrange(nx, ny):
                res += f(nx, ny, count - 1)
        dp[x][y][count] = res

    return dp[x][y][count]


def inrange(x, y):
    # 이동 가능한 범위를 벗어나는지 여부를 반환합니다.
    return -14 <= x <= 14 and -7 <= y <= 7


if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        dp = [[[-1]*15 for _ in range(15)] for _ in range(29)]
        print(f(0, 0, n))
