import sys
input = sys.stdin.readline

n = int(input())

arr = [0 for _ in range(n+1)]
arr[0] = 1
arr[1] = 1

for i in range(2, n+1):
    arr[i] = arr[i-1]+arr[i-2]*2

if n % 2 == 1:
    print((arr[n]+arr[n//2])//2)
else:
    print((arr[n]+arr[n//2]+arr[n//2-1]*2)//2)
