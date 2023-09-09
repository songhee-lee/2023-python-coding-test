"""
ATM 앞에 N명의 사람들이 줄을 섰고, i번 사람이 돈을 인출하는데 Pi분이 걸린다.
그리고 i번째 사람은 i-1번째 사람이 돈을 뽑기까지 P1 + ... + Pi-1 분을 기다려야한다.
각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값 구하기

1 <= N <= 1000
"""

N = int(input())
P = list(map(int, input().split()))
P.sort()    # 오름차순으로 정렬
answer = 0  # 전체 필요한 시간
for i in range(N) :
    # i번째 사람이 돈을 인출하는데 걸리는 시간은 (N-i)번 더해진다.
    answer += (N-i) * P[i]
print(answer)