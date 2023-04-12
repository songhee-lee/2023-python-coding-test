"""
- 일직선의 식량창고를 선택적으로 약탈
- 개미 전사가 정찰병에게 들키지 않으려면 한 칸 떨어진 식량 창고를 약탈해야 함
""" 

N = int(input())    # 식량창고 개수
foods = list(map(int, input().split())) # 저장된 식량 개수

# dp[x] : x개 식량 창고에서 최대 식량
dp = [0] * N

# 초깃값 설정
dp[0] = foods[0]
dp[1] = max(foods[0], foods[1])

# Bottom-up
for i in range(2, N):
    # i번째 창고를 턴다 vs 털지 않는다
    dp[i] = max(dp[i-2]+foods[i], dp[i-1])

print(dp[N-1])

