'''
n = 아이들 수
m = 놀이기구의 수
mid로 여태까지 태운 아이들의 명수와 N이 가장 가까운 시간을 뽑아내서,
정확히 N명을 태웠을 경우 어떤 놀이기구를 타는 지 확인
'''

N, M = map(int, input().split())
t = list(map(int, input().split()))

l = 1
r = 10**20
max_m = max_s = 0

while l <= r:
    mid = (l+r)//2
    s = sum((mid-1)//x + 1 for x in t)
    if s < N:
        if max_m < mid:
            max_m = mid
            max_s = s
        l = mid + 1
    else:
        r = mid - 1

for i, k in enumerate(t):
    if max_m % k == 0:
        max_s += 1
        if max_s == N:
            print(i+1)
            break
