""" 
- N명의 아이들이 M종류 놀이기구를 기다리고 있다.
- 놀이기구는 각각 운행 시간이 정해져 있다
- 동시에 비어 있으면 더 작은 번호의 놀이기구를 탑승
- 마지막 아이가 타게 되는 놀이기구의 번호는?
"""

N, M = map(int, input().split())
rides = list(map(int, input().split()))

# 예외 - 모두가 하나씩 놀이기구 타기 가능
if N <= M :
    print(N)
# 이분 탐색
else:
    # N명 모두 태울 수 있는 최소 time 구하기
    s, e = 0, int(6e10)  # N명을 모두 태울 수 있는 time (초) 최소 / 최대
    time = None
    while s <= e :
        m = (s+e) // 2
        cnt = M     # 0초에 M개 놀이기구에 한 명 씩 탑승

        # m초 동안 각 놀이기구가 태울 수 있는 인원 수 구하기
        for i in range(M):
            cnt += m // rides[i]    
        
        # N명 태울 수 있으면 정답
        if cnt >= N :
            time = m
            e = m-1
        else:
            s = m+1

    print(time)
    # time-1 초까지 탑승한 학생 수
    cnt = M
    for i in range(M):
        cnt += (time-1) // rides[i]
    print(cnt)

    # time 에 탑승한 학생 수
    for i in range(M):
        if time % rides[i] == 0:
            cnt += 1
        if cnt == N:
            print(i+1)
            break
