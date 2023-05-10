'''
수열 중 한개 이상 선택시
선택 수의 최대공약수가 1이 되는 것

'''


import sys  # 모듈을 불러온다

input = sys.stdin.readline  # 표준 입력 대신 sys.stdin.readline을 사용한다

N = int(input())  # 정수형으로 입력값을 받아 N에 할당한다

L = [int(input()) for i in range(N)]  # N개의 정수형 입력값을 받아 리스트 L에 저장한다

M = max(L)  # L 리스트의 최댓값을 M에 할당한다

DP = [0]*(1+M)  # M+1 크기의 리스트 DP를 생성하고 0으로 초기화한다

for i in L:  # 리스트 L을 순회한다
    for j in range(1, M+1):  # 1부터 M까지 반복한다
        if DP[j]:  # DP[j] 값이 존재하면 실행한다
            x, y = i, j  # x에 i 값을, y에 j 값을 할당한다
            while x:  # x 값이 0이 아닐 때까지 반복한다
                x, y = y % x, x  # y를 x로 나눈 나머지를 x 값으로, x를 y 값으로 변경한다
            # y가 gcd
            # DP[y]에 (DP[y]+DP[j])%10000003 값을 할당한다
            DP[y] = (DP[y]+DP[j]) % 10000003
    DP[i] += 1  # DP[i]에 1을 더한 값을 할당한다

print(DP[1])  # DP[1] 값을 출력한다
