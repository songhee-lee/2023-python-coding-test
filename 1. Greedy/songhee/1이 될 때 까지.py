"""Psuedo Code

1. 수 입력 받기
2. N % K 만큼 빼고, K 로 나누기 반복 

"""

# 입력 받기
N, K = map(int, input().split())

# 계산
cnt = 0
while N > 1:   # N이 1이 되면 멈춤

    x = N % K    # target 

    if N < K :      # 더이상 K로 나눌 수 없는 경우
        cnt += x-1

    else:    # K로 나누어 떨어지질 때까지 1씩 빼고, 나누기
        cnt += x + 1
    
    N = N // K

print(cnt)
