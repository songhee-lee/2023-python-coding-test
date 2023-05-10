# DP
"""
n = int(input())
arr = list(map(int,input().split()))
d = [1] * n

for i in range(n):
    for j in range(i):
        if arr[i]>arr[j] : d[i] = max(d[i],d[j]+1)

print(max(d))
"""

# 이분 탐색
n = int(input())
arr = [0]+list(map(int,input().split()))
memorization = [0]

for a in arr:
    if memorization[-1] < a : memorization.append(a)
    else:
        start,end = 0,len(memorization)
        while start<=end:
            mid = (start+end)//2
            if memorization[mid] < a : start = mid+1
            else : end = mid-1
        memorization[start]=a

print(len(memorization)-1)