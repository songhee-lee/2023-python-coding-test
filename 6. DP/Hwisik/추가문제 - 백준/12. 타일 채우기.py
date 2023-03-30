'''
[문제]
- 3xN 크기의 벽을 2x1, 1x2 크기의 타일로 채우는 방법의 수를 구하라.

[점화식]
- dp[i] += dp[i - j] * 2 + dp[i - j] * 3
    -> 단, dp[i - j] * 2 는 j == 2일 때, dp[i - j] * 3은 j != 2일 때
    -> 가로가 i일 때 타일로 채우는 방법의 수
    -> 윗면, 아랫면을 모두 1 * 2 타일로 채우는 경우의 수는 i마다 2가지이다.
        (즉, 새로운 형태의 타일 배치가 2가지이다.)
-> ✅ 다시 풀기
-> 그림 그리기
'''

n = int(input())

if n % 2 == 1:
    print(0)
else:
    dp = [0] * (31)
    dp[0] = 1
    dp[2] = 3
    
    for i in range(3, n + 1):
        if i % 2 == 1:
            continue
        dp[i] += dp[i - j] * 3
        
        for j in range(4, i + 1, 2):
            dp[i] += dp[i - j] * 2
                
    print(dp[n])