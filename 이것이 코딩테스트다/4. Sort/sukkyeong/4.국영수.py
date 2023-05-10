'''
학생이름,
국영수 점수 주어짐
1. 국어 점수 감소 순서
2. 국어 == 영어, 수학 점수 감소 순서
3. 국어 == 영어 == 수학, 이름 사전순

배열을 만들어서
a[0], a[1], a[2] a[3]를 돌면서 반복문 비교


'''

N = int(input())
arr = []

for _ in range(N):
    a, b, c, d = list(map(str, input().split()))
    arr.append([a, int(b), int(c), int(d)])

arr.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for i in arr:
    print(i[0])
