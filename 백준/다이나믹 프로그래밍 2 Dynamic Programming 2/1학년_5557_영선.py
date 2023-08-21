#입력1 : 숫자 갯수 n
#입력2 : 공백 구분 정수 n개

#출력 : 올바른 등식의 갯수 < 2^63 -1

import sys

n = int(input())

num = list(map(int, sys.stdin.readline().split()))

cnt = [ [0]*21 for _ in range(n-1)]

#첫 번째 수는 0번째 num과 같음 -> 경우의 수 1
#cnt[i][j] : i번째까지 계산하여 j를 만들 수 있는 경우의 수
cnt[0][num[0]] = 1


for i in range(1, n-1):
    for j in range(21):
        # - 연산
        if j - num[i] >= 0:
            cnt[i][j] += cnt[i-1][j-num[i]]

        # + 연산
        if j + num[i] <= 20:
            cnt[i][j] += cnt[i-1][j+num[i]]

#n-2번째가 num[-1]과 같을 총 경우의 수
print(cnt[n-2][num[-1]])
