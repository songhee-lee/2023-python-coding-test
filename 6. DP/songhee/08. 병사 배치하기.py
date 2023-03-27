"""
- N명의 병사는 각각 전투력을 갖고 내림차순으로 배치하려고 함
- 남아있는 병사의 수가 최대가 되도록 하는 방법
""" 

N = int(input())
soldier = list(map(int, input().split()))

# dp[x] : x번째 병사부터 배치할 때 최대 병사의 수
dp = [1] * N

# Bottom-up
for i in range(1, N):
    for j in range(i):
        if soldier[j] > soldier[i] :
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))

