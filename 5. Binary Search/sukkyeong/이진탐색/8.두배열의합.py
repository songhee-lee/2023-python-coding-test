from collections import defaultdict

T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

sum_A, sum_B = [0], [0]
for i in range(n):
    sum_A.append(sum_A[i] + A[i])
for i in range(m):
    sum_B.append(sum_B[i] + B[i])

dic = defaultdict(int)
for i in range(n + 1):
    for j in range(i + 1, n + 1):
        dic[sum_A[j] - sum_A[i]] += 1

result = 0
for i in range(m + 1):
    for j in range(i + 1, m + 1):
        if T - (sum_B[j] - sum_B[i]) in dic:
            result += dic[T - (sum_B[j] - sum_B[i])]

print(result)
