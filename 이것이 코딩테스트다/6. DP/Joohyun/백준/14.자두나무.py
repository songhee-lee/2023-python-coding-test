from sys import stdin
input = stdin.readline

t,w = map(int,input().split())          # t:자두가 떨어지는 시간, w:자두가 움직이는 최대 횟수
dp = [[0]*(w+1) for _ in range(t+1)]    # 행:시간  열:움직임횟수

plums = [0]+[int(input()) for _ in range(t)]    # 자두 정보

for i in range(1,t+1):              # i:행
    # 안움직였을 경우 (위치:1번)
    if plums[i]==1:                 # 자두가 1번에서 떨어질 때
        dp[i][0]=dp[i-1][0]+1
    else: dp[i][0]=dp[i-1][0]       # 자두가 1번에서 

    # 이동 횟수를 1번부터 n번까지 움직이면서 체크
    for j in range(1,w+1):          # j:열
        if j>i: break

        # 자두가 1번에서 떨어졌을 경우
        if plums[i]==1 and j%2==0 :                     # 짝수번째 움직임일 때 -> 1번에 있을 때
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-1])+1   # 이전 위치가 1번이었을 경우, 이전 위치가 2번이었을 경우
        
        # 자두가 2번에서 떨어졌을 경우
        elif plums[i]==2 and j%2==1 :                     # 홀수번째 움직임일 때 -> 2번에 있을 때
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1])+1  # 이전 위치가 2번이었을 경우, 이전 위치가 1번이었을 경우
        
        # 안 먹음
        else:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-1])

print(max(dp[-1]))