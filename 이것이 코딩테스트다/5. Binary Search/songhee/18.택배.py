""" 
- 트럭은 되돌아가지 않음
- 트럭 한 대로 보낼 수 있는 최대 박스 수 구하기
"""
from collections import defaultdict

# 입력 받기
N, C = map(int, input().split())    # 마을 수, 트럭 용량
M = int(input())    # 보내는 박스 정보 개수

info = []
for _ in range(M):
    fr, to, box = map(int, input().split())
    info.append((fr, to, box))  # (보내는 마을, 받는 마을, 박스 개수)

# 받는 마을 순으로 정렬
info.sort(key=lambda x: x[1])

# 각 마을에서 배달 가능한 용량 초기화
capacity = [C] * N
ans = 0

# 각 요청 사항 보면서 가장 가까운 도착지 박스부터 싣기
for fr, to, box in info:
    mini = C    # 현재 최대 용량이라고 가정

    # 출발지 -> 도착지 사이에서 보낼 수 있는 box 양 확인
    for i in range(fr, to):
        mini = min(mini, capacity[i], box)
    
    # 출발지 -> 도착지 까지 보낼 수 있는 box 양 업데이트 
    for i in range(fr, to):
        capacity[i] -= mini
    
    # 보낸 박스 양 추가
    ans += mini

print(ans)