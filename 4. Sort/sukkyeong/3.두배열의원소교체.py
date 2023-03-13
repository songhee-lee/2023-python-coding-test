'''
a = [1,2,5,4,3]
b = [5,5,6,6,5]
-> a = [6,6,5,4,5]
-> b = [5,5,1,2,3]

1. a 배열을 오름차순하고, b 배열을 내림차순함
2. k개만큼 서로 원소를 바꾸고
3. a의 sum을 리턴
'''
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(revese=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break
print(sum(a))
