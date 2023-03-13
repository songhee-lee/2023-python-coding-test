'''
- 입력을 받아서 리스트에 저장한다.
- 리스트를 내림차순 정렬 한다.
- 출력
'''

n = int(input())

arr = []
for _ in range(n):
    arr.append(int(input()))

# 내림차순 정렬
arr.sort(key=lambda x: -x) # or sort(reverse=True)

print(*arr)