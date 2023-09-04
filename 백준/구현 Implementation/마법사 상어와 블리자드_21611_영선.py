#입력1 : 영토의 크기 N, M
#입력2 : NxM 사람수 1~100
#입력3 : K 인구 수를 궁금해하는 직사각형 범위의 개수 <=100,000
#입력4 : K줄만큼 직사각형 범위 x1,y1,x2,y2

#출력 : k개의 줄에 순서대로 주어진 직사각형 범위 내에 살고 있는 사람 수의 합
import sys

n, m = map(int, sys.stdin.readline().split())

board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

k = int(input())

#원소를 하나하나 구하면 n*m*k의 시간복잡도 요구
#누적합 이용
sum_arr = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        sum_arr[i][j] = board[i-1][j-1] + sum_arr[i-1][j] + sum_arr[i][j-1] - sum_arr[i-1][j-1]

#x2,y2까지 누적합에서 제외되는 부분의 누적합을 빼는데
#교차되는 부분을 두번 빼게 되므로 한 번 더해
for _ in range(k):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    print(sum_arr[x2][y2] - sum_arr[x1-1][y2] - sum_arr[x2][y1-1] + sum_arr[x1-1][y1-1])
