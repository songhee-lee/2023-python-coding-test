from sys import stdin
input = stdin.readline

n = int(input())
numbers=list(map(int,input().split()))

dp=[[0]*21 for _ in range(n)]   # 행(i):numbers의 인덱스, 열(j):해당 얀덱스까지 계산했을 때 j가 나올 경우의 수

dp[0][numbers[0]]=1             # idx=0일 때 결과값이 numbers[0]이 될 경우의 수는 항상 1

for i in range(1,n-1):
    for j in range(21):
        if dp[i-1][j] :
            # i-1번째 numbers까지 계산한 결과가 j일 때
            if j+numbers[i]<=20 : dp[i][j+numbers[i]]+=dp[i-1][j]  # j에 i번째 수를 더한 값이 20 이하일 경우, UPDATE
            if j-numbers[i]>=0  : dp[i][j-numbers[i]]+=dp[i-1][j]  # j에 i번째 수를 뺀 값이 0 이상일 경우, UPDATE

print(dp[n-2][numbers[n-1]])    # 출력 : n-2번째 numbers까지 계산한 결과가 numbers[n-1]인 경우의 수