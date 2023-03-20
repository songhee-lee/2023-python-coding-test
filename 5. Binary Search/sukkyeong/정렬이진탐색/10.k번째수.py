'''
(a/행번호)가 그 행에서 구하고자 하는 개수
(a/행번호)가 n보다 크면 n
이분탐색
'''

n = int(input())
k = int(input())


def binary_search(target, start, end):
    while (start <= end):
        mid = (start + end) // 2

        cnt = 0
        for i in range(1, n+1):
            cnt += min(mid//i, n)

        if cnt >= target:
            end = mid-1
        else:
            start = mid+1
    return start


print(binary_search(k, 1, n*n))
