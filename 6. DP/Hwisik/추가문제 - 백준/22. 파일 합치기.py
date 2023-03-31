'''
[문제]
- 소설의 각 장을 합쳐서 파일 하나로 만들려고 한다.
- 파일들을 하나의 파일로 합칠 때 필요한 최소비용을 계산하라.

[점화식]
- 

'''

t = int(input())

for _ in range(t):
    k = int(input())
    files = list(map(int, input().split()))
    