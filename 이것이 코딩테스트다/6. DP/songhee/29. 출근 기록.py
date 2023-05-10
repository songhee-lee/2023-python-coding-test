"""
 -  A : 매일 출근 가능
    B : 2일 한 번 출근
    C : 3일 한 번 출근
 - 출근 기록 S의 순열 중 올바른 출근 기록 출력하기
"""
from collections import Counter

string = input()
S = Counter(string)
a, b, c = S['A'], S['B'], S['C']
n = a+b+c

if n == 1:
    print(string)
else:
    # dp[i] : i번째까지의 올바른 출근 기록
    dp = ['' for i in range(n+1)]
    flag_b, flag_c = 1, 2   # B와 C가 출근한 날짜

    for i in range(1, n+1):
        if c > b and flag_c >= 2:
            dp[i] = dp[i-1]+'C'
            c -= 1
            flag_b, flag_c = flag_b+1, 0
        elif b > 0 and flag_b >= 1:
            dp[i] = dp[i-1]+'B'
            b -= 1
            flag_b, flag_c = 0, flag_c+1
        elif a > 0:
            dp[i] = dp[i-1]+'A'
            a -= 1
            flag_b, flag_c = flag_b+1, flag_c+1 
        else:
            dp[n] = -1
            break
    print(dp[n])