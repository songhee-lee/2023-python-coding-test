'''

'''
# 입력
n = int(input())
a = list(map(int, input().split()))
m = int(input())
arr = list(map(int, input().split()))
a.sort()

for num in arr:
    front, back = 0, n-1
    isExist = False

    while front <= back:
        mid = (front + back) // 2
        if num == a[mid]:
            isExist = True
            print(1)
            break
        elif num > a[mid]:
            front = mid + 1
        else:
            back = mid - 1
    if not isExist:
        print(0)
