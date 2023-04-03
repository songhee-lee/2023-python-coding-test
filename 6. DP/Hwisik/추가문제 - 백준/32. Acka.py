'''
[문제]
- 총 S개의 곡이 있다. 각각의 곡은 세 사람중 적어도 한 명이 불러야 한다.
- 즉, 어떤 곡은 두 사람이 불러도 되고, 세 사람이 모두 함께 불러도 된다.
- 세 사람이 녹음해야 하는 곡의 수가 주어질 때, 앨범을 만들 수 있는 방법의 수를 구하시오.
- 두 앨범 A와 B가 있을 때, 참여한 사람이 다른 곡이 존재한다면, 두 앨범은 다른 앨범이라고 한다.

[점화식]
- dp[s][a][b][c] = dp[s - 1][a - 1][b][c] + dp[s - 1][a][b - 1][c] + dp[s - 1][a][b][c - 1] + dp[s - 1][a - 1][b - 1][c] + dp[s - 1][a - 1][b][c - 1] + dp[s - 1][a][b - 1][c - 1] + dp[s - 1][a - 1][b - 1][c - 1]

✅ 답 참고함, 다시 풀기
'''

def helper(s, a, b, c):
    if s == 0:
        if a == b == c == 0:
            return 1
        else:
            return 0
    
    if a < 0 and b < 0 and c < 0:
        return 0
    
    if dp[s][a][b][c] != -1:
        return dp[s][a][b][c]
    
    dp[s][a][b][c] = 0
    for i in range(2):
        for j in range(2):
            for k in range(2):
                if i + j + k == 0:
                    continue
                dp[s][a][b][c] += helper(s - 1, a - i, b - j, c - k)
    dp[s][a][b][c] %= 1_000_000_007
    
    return dp[s][a][b][c]

s, a, b, c = map(int, input().split())
dp = [[[[-1 for _ in range(51)] for _ in range(51)] for _ in range(51)] for _ in range(51)]

print(helper(s, a, b, c))