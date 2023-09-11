n = int(input())
arr = sorted(list(map(int, input().split())))

answer = 0
for i in range(1, n):
  arr[i] += arr[i - 1]
  answer += arr[i]
  
print(answer + arr[0])