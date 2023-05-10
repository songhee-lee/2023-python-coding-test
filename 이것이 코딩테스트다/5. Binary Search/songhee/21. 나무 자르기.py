"""
- 나무 M미터 필요
- 절단기 높이 H
"""

# 입력 받기
N, M = map(int, input().split())            # 나무 수, 필요한 나무 길이
trees = list(map(int, input().split()))     # 나무의 높이

trees.sort()

# 절단기 높이 정하기
s, e = 0, trees[-1]
answer = 0
while s <= e:
    h = (s+e) // 2
    
    # 전체 나무의 합
    tree_sum = sum([ x-h for x in trees if x > h ]) 

    if tree_sum == M :
        answer = h
        break
    elif tree_sum > M : # 나무 길이가 더 많으면
        answer = h
        s = h+1         ## 절단기 높이 up
    else:
        e = h-1         # 나무 길이가 더 적으면 절단기 높이 down

print(answer)