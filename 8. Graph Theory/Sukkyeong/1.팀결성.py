'''
같은 팀원인지 확인
'''
#속한 곳 찾기
def solution(parent, x):
    if parent[x] !=x:
        parent[x] = solution(parent, parent[x])
    return parent[x]

#두 원소가 속한 곳 찾기
def all(parent, a, b):
    a = all(parent, a)
    b = all(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [0]*[n+1]

for i in range(0, n+1):
    parent[i] = i

for i in range(m):
    oper, a, b = map(int, input().split())
    if oper == 0:
        all(parent, a, b)
    elif oper == 1:
        if solution(parent, a) == all(parent, b):
            print('yes')
        else:
            print('no')