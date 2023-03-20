'''


'''


import sys

n = int(sys.stdin.readline())
cards = sorted(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline())
checks = list(map(int, sys.stdin.readline().split()))

for check in checks:
    low, high = 0, n-1
    exist = False
    while low <= high:
        mid = (low + high)//2
        if cards[mid] > check:
            high = mid - 1
        elif cards[mid] < check:
            low = mid + 1
        else:
            exist = True
            break
    print(1 if exist else 0, end=' ')
