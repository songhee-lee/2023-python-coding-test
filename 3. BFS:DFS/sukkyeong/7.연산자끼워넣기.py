from itertools import permutations

n = int(input())
a = list(map(int, input().split()))
op = list(map(int, input().split()))

# 모든 연산자 조합 생성
op_list = []
for i in range(4):
    op_list.extend([i]*op[i])
perm_op = set(permutations(op_list, n-1))

min_ans = float('inf')
max_ans = float('-inf')

# 모든 연산자 조합에 대해 계산하여 최댓값과 최솟값 찾기
for p in perm_op:
    cur = a[0]
    for i in range(n-1):
        if p[i] == 0:
            cur += a[i+1]
        elif p[i] == 1:
            cur -= a[i+1]
        elif p[i] == 2:
            cur *= a[i+1]
        else:
            if cur < 0:
                cur = -(-cur//a[i+1])
            else:
                cur //= a[i+1]
    max_ans = max(max_ans, cur)
    min_ans = min(min_ans, cur)

print(max_ans)
print(min_ans)
