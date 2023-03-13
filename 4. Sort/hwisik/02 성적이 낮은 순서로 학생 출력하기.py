'''
- 입력을 받아서 리스트에 저장한다.
- 점수를 기준으로, 오름차순 정렬을 수행한다.
- 출력한다.
'''
n = int(input())
arr = []

for _ in range(n):
    input_data = input().split()
    arr.append((input_data[0], input_data[1]))

# 점수 기준, 오름차순 정렬
arr.sort(key=lambda x:x[1])

for i in range(n):
    print(arr[i][0], end = ' ')