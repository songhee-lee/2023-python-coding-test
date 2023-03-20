'''
left를 0으로, 주어진 배열에서 가장 큰 수를 right로,
mid를 (left + right)/2로 지정한다.
그리고 주어진 배열 첫 번째부터 마지막까지 탐색하면서
현재까지의 (최댓값 - 최솟값)이 mid보다 큰 경우
이전 인덱스까지를 한 구간으로 하며 배열이 끝날 때까지
반복하여 생기는 구간의 수를 구한다.
그리고 계산한 구간의 수가 주어진 구간 k보다 작거나 같으면
기준 값인 mid를 줄이고 구간 k보다 크면 기준 값인 mid를 늘려
구간의 수를 조절한다.
구간의 수가 주어진 k보다 크거나 같을 경우
기준값인 mid값을 비교하여 현재 저장된 최댓값과 mid를 비교하여 최댓값을 저장한다.

'''


import sys
input = sys.stdin.readline


def isValid(midValue):
    global result
    low = arr[0]
    high = arr[0]
    d = 1

    for i in arr:
        if high < i:
            high = i

        if low > i:
            low = i

        if high - low > midValue:
            d += 1
            low = i
            high = i

    return m >= d


n, m = map(int, input().split())

arr = list(map(int, input().split()))

r = max(arr)
l = 0

result = r
while l <= r:
    mid = (l + r) // 2

    if isValid(mid):
        r = mid - 1
        result = min(result, mid)
    else:
        l = mid + 1

print(result)
