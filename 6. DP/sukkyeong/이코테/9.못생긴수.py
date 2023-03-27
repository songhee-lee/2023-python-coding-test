'''
2,3.5의 배수에(못생긴 수에)
2,3,5를 곱한 수 또한 못생긴 수에 해당함
각 가장 작은 못생긴 수부터 오름차순으로 확인,
각 배수를 곱한 값도 못생긴 수가 되도록 처리

'''

n = int(input())

answer = [0] * n
answer[0] = 1

idx2, idx3, idx5 = 0, 0, 0
multi2, multi3, multi5 = 2, 3, 5

for i in range(1, n):
    answer[i] = min(multi2, multi3, multi5)
    if answer[i] == multi2:
        idx2 += 1
        multi2 = answer[idx2]*2
    if answer[i] == multi3:
        idx3 += 1
        multi3 = answer[idx3]*3
    if answer[i] == multi5:
        idx5 += 1
        multi5 = answer[idx5]*5

print(answer[n-1])
