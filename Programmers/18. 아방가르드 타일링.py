''' ref
DP(x) = DP(x-1) + 2*DP(x-2) + 6*DP(x-3) + DP(x-4) - DP(x-6)
'''
import sys
sys.setrecursionlimit(10**6)
DP = [0]*100001

def solution(n):

    answer = block(n) % 1000000007

    return answer

def block(n):
    answer = 0

    if n==1:
        DP[1]=1
        return 1
    if n==2:
        DP[2]=3
        return 3
    if n==3:
        DP[3]=10
        return 10
    if n==4:
        DP[4]=23
        return 23
    if n==5:
        DP[5]=62
        return 62
    if n==6:
        DP[6]=170
        return 170

    if DP[n-1]:
        answer += DP[n-1]
    else:
        answer += block(n-1)
    if DP[n-2]:
        answer += DP[n-2]*2
    else:
        answer += block(n-2)*2
    if DP[n-3]:
        answer += DP[n-3]*6
    else:
        answer += block(n-3)*6
    if DP[n-4]:
        answer += DP[n-4]*1
    else:
        answer += block(n-4)*1
    if DP[n-6]:
        answer -= DP[n-6]*1
    else:
        answer -= block(n-6)*1

    DP[n]=answer

    return answer