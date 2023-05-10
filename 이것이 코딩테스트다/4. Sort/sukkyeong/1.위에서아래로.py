'''
수열의 수를 큰 수부터 작은 수의 순서로 정렬
내림차순으로 정렬
'''
n = int(input())

array = []
for i in range(n):
    array.append(int(input()))

array = sorted(array, reverse=True)

for i in array:
    print(i, end=' ')
