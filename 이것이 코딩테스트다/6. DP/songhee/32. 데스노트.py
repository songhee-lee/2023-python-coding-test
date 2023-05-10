"""
- 데스노트에 N명 이름 적기
- 정해진 순서로, 위->아래, 왼->오른 차례로 적기
- 이름 사이에 빈칸
- 각 줄의 끝에 남은 칸의 제곱합이 최소가 되도록 하기 (마지막 칸 제외) 
"""

n, m = map(int, input().split())
names = [int(input()) for _ in range(n)]

# dp[i] : i번째까지 썼을 때 최솟값
dp = [float('inf')]*(n+1)
dp[n] = 0

def counting(i):
    if dp[i] != float('inf'):
        return dp[i]
    
    # 새로운 줄에 현재 이름 적고 난 공간 개수
    buffer = m - names[i]

    for idx in range(i+1, n+1):
        # 현재 줄에 이름을 적을 수 있으면
        if buffer >= 0:
            if idx == n :
                dp[i] = 0 
                break   # 마지막이면 끝
            # 다음 줄에 이름 쓸 때랑 현재 값 비교 
            dp[i] = min(dp[i], buffer*buffer + counting(idx))
            buffer -= names[idx] + 1
    return dp[i]

print(counting(0))