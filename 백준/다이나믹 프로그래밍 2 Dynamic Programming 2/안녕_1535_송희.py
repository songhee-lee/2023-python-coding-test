"""
세준이를 생각해준 사람이 1~N번까지 있을 때, i번 사람에게 인사하면 L[i] 만큼의 체력을 잃고 J[i]만큼의 기쁨을 얻는다.
100의 체력 내에서 느낄 수 있는 최대한의 기쁨은?
1 <= N <= 20

알고리즘 : 배낭 문제 (0-1 Knapsack)
"""

N = int(input())
L = list(map(int, input().split()))
J = list(map(int, input().split()))

dp = [[0]*101 for _ in range(N+1)]

for i in range(1, N+1) :
    life, joy = L[i-1], J[i-1]

    for j in range(1, 101) :        # 체력이 1~100일 경우
        if life <= j :              # 남은 체력으로 현재 사람 만날 수 있다면
            # 현재 사람 안만나기 vs 만나기 중 더 기쁨이 큰 경우 선택 
            dp[i][j] = max(dp[i-1][j], joy + dp[i-1][j-life])
        else :                      # 남은 체력으로는 못만나는 경우
            dp[i][j] = dp[i-1][j]
            
print(dp[N][100])