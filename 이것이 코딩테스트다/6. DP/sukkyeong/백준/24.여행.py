'''
n, m, k를 입력받는다.
항공편에 해당하는 리스트 airline을 (n+1)*(n+1)의 크기로 선언하고 0으로 채운다.
dp리스트를 (n+1)*(m+1)의 크기로 선언한다.
k번 반복하는 for문을 돌린다.
-> a, b, c를 입력받는다.
-> airline[a][b]를 airline[a][b]와 c 중 더 큰 값으로 갱신한다.
2부터 n까지의 i에 대한 for문을 돌린다.
-> 3부터 m까지의 j에 대한 for문을 돌린다.
--> 1부터 i-1까지의 l에 대한 for문을 돌린다.
---> 만약 airline[l][i]가 0이 아니고, dp[l][j-1]이 0이 아닐 경우,
----> dp[i][j]를 dp[l][j-1]+airline[l][i]와 dp[i][j] 중 더 큰 값으로 갱신한다.
dp[n]에서의 최댓값을 출력한다.
'''
import sys  # 모듈을 불러온다

input = sys.stdin.readline  # 표준 입력 대신 sys.stdin.readline을 사용한다

n, m, k = map(int, input().split())  # 정수형으로 입력값을 받아 각각 n, m, k에 할당한다

# n+1 x n+1 크기의 2차원 리스트 airline을 생성하고 0으로 초기화한다
airline = [[0]*(n+1) for _ in range(n+1)]

# n+1 x m+1 크기의 2차원 리스트 dp를 생성하고 0으로 초기화한다
dp = [[0]*(m+1) for _ in range(n+1)]

for _ in range(k):  # k번 반복한다
    a, b, c = map(int, input().split())  # 정수형으로 입력값을 받아 각각 a, b, c에 할당한다
    # airline[a][b]에 c와 현재 저장된 값 중 더 큰 값을 할당한다
    airline[a][b] = max(airline[a][b], c)

for i in range(2, n+1):  # i를 2부터 n까지 반복한다
    dp[i][2] = airline[1][i]  # dp[i][2]에 airline[1][i] 값을 할당한다

for i in range(2, n+1):  # i를 2부터 n까지 반복한다
    for j in range(3, m+1):  # j를 3부터 m까지 반복한다
        for l in range(1, i):  # l을 1부터 i-1까지 반복한다
            if airline[l][i] and dp[l][j-1]:  # airline[l][i]와 dp[l][j-1] 값이 모두 존재하면 실행한다
                # dp[i][j]에 dp[l][j-1]+airline[l][i]와 현재 저장된 값 중 더 큰 값을 할당한다
                dp[i][j] = max(dp[l][j-1]+airline[l][i], dp[i][j])

print(max(dp[n]))  # dp[n]에서 최댓값을 출력한다
