'''
[문제]
- 마지막 두 숫자 사이에는 '='을 넣고, 나머지 숫자 사이에는 '+' 또는 '-'를 넣어 등식을 만들려고 한다.
- 중간에 나오는 수는 모두 0 이상 20 이하이어야 한다.(음수가 나오면 안됨)
- 만들 수 있는 올바른 등식의 수를 구하라.

[점화식]
- dp[i][j] = _list의 i번째 숫자를 사용해서 숫자 j를 만들 수 있는 경우의 수
    -> i는 _list의 크기 + 1, j는 0부터 20까지의 숫자
    -> 단, i는 0부터 시작한다.(0-index)
'''

n = int(input())
_list = list(map(int, input().split()))

dp = [[0] * 21 for _ in range(n)]

# _list의 첫번째 숫자는 무조건 1이다.(등식의 첫번째 숫자이므로)
dp[0][_list[0]] = 1

# _list의 1번째 숫자부터 n - 2번째 숫자까지
for i in range(1, n - 1):
    for num in range(21): # 중간에 나오는 수는 모두 0 이상 20이하
        
        # num을 만들 수 있다면,
        if dp[i - 1][num] != 0:
            _add = num + _list[i] # +
            _sub = num - _list[i] # -
            
            # 경우의 수를 더해준다.
            if _add <= 20:
                dp[i][_add] += dp[i - 1][num]
            if _sub >= 0:
                dp[i][_sub] += dp[i - 1][num]

# n - 2번째 숫자를 사용해서 _list의 마지막 숫자를 만들 수 있는 경우의 수를 구한다.
print(dp[n - 2][_list[-1]])