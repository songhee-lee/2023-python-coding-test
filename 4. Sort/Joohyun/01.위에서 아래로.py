n = int(input())
arr = [int(input()) for i in range(n)]
print(*sorted(arr,reverse=True))