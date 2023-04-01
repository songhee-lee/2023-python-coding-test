""" 
- 두 파일을 합칠  때 필요한 비용은 두 파일 크기의 합
- 하나의 파일을 완성하는데 필요한 비용의 총 합 계산하기
"""

for _ in range(int(input())):
    K = int(input())
    f = list(map(int, input().split()))

    # files[i][j] : i~j까지의 파일 크기의 합
    files = [ [0]*K for _ in range(K) ]
    