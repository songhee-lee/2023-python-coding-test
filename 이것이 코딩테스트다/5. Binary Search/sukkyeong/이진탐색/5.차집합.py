'''
집합a에는 속하면서
집합b에는 속하지 않는 모든 원소 구하기
'''
n = map(int, input().split())

a = set(map(int, input().split()))
b = set(map(int, input().split()))

res = []
for i in a:
    if i not in b:
        res.append(i)

res.sort()
print(len(res))

if len(res) != 0:
    print(*(res))
