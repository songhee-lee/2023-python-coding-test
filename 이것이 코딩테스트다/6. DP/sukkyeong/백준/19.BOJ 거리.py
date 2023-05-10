# 입력값 받기
n = int(input())
lst = input()

# MAX값 설정
MAX = 999999999

# dp 초기화
dp = [MAX] * n

# 이전 값 구하기


def get_prev(x):
    if x == "B":
        return "J"
    elif x == "O":
        return "B"
    elif x == "J":
        return "O"


# 초기값 설정
dp[0] = 0

# dp 계산하기
for i in range(1, n):
    prev = get_prev(lst[i])
    for j in range(i):
        if lst[j] == prev:
            dp[i] = min(dp[i], dp[j] + pow(i - j, 2))

# 결과 출력하기
print(dp[n - 1] if dp[n - 1] != MAX else -1)
