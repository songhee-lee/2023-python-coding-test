'''
- 배열 A는 오름차순 정렬
- 배열 B는 내림차순 정렬
- 인덱스: 0부터 K - 1까지, A의 원소가 B의 원소보다 작다면, 배열 A와 배열 B의 원소를 바꾼다.
'''

n, k = map(int, input().split())

a_arr = list(map(int, input().split()))
b_arr = list(map(int, input().split()))

# A는 오름차순 정렬, B는 내림차순 정렬
a_arr.sort()
b_arr.sort(reverse=True)

for i in range(k):
    # A의 원소가 B의 원소보다 작다면
    if a_arr[i] < b_arr[i]:
        # swap
        a_arr[i], b_arr[i] = b_arr[i], a_arr[i]

print(sum(a_arr))