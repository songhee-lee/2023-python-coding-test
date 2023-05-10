'''
 x + y + z = k 일 때, x + y = k - z
'''

import sys
input = sys.stdin.readline
N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()

arr_sum = set()
for x in arr:
    for y in arr:
        arr_sum.add(x+y)


def check():
    global answer
    for i in range(N-1, -1, -1):
        for j in range(i+1):
            if arr[i]-arr[j] in arr_sum:
                answer = arr[i]
                return


answer = 0
check()
print(answer)
