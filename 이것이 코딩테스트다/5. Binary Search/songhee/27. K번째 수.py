""" 
- A[i][j] = i x j
- 오름차순 정렬했을 때 B[k] 구하기
"""

N = int(input())
K = int(input())

s, e = 1, K
while s <= e:
    m = (s+e) // 2

    cnt = 0
    # m 보다 작거나 같은 숫자 개수 세기
    for i in range(1, N+1):
        cnt += min(m//i, N)
    
    if cnt >= K :
        answer = m
        e = m-1
    else:
        s = m+1
print(s)
""" 메모리 제한
lst = [ i*j for i in range(1, N+1) for j in range(1, N+1)]
lst.sort()

print(lst[K])
"""


