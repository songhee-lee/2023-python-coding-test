'''
2*n의 크기의 직사각형을
1*2, 2*1타일로 채우는 방법의 수

'''
n = int(input())
res = [0] * 1001
res[1] = 1
res[2] = 2
for i in range(3, n+1):
    res[i] = res[i-1] + res[i-2]
print(res[n] % 10007)
