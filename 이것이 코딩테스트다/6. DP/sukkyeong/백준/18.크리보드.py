'''
저 초기값으로 i번째 인덱스에는 A를 i번 누른 횟수로 초기화를 하고

버퍼에 있는 값을 복사하기 까지 총 3번에 커맨드 횟수가 필요하므로

컨트롤 v를 한번 두번 세번 누른 최대값을 비교 후 갱신해주면 된다.

그 이유는 이미 앞에서 최대값을 갱신했기때문에 커맨드 명령횟수 3번까지만 체크해주면 된다.

dp[i] = max ( dp[i-3]*2, dp[i-4]*3, dp[i-5]*4)  // v를 한 번 누른경우 , 두 번 누른경우 , 세 번 누른경우
'''


import sys
input = sys.stdin.readline
n = int(input())
dp = [i for i in range(0, 102)]

for i in range(6, 101):
    dp[i] = max(dp[i-3]*2, max(dp[i-4]*3, dp[i-5]*4))
print(dp[n])
