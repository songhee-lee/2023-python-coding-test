#입력1 : n 사람 수 <= 20
#입력2 : 각 사람에게 인사할때 잃는 체력
#입력3 : 각 사람에게 얻는 기쁨

#출력 : 세준이가 얻을 수 있는 최대 기쁨
'''
i 번 사람에게 인사하면 L[i]만큼 체력이 사라짐, J[i]만큼 기쁨 생김
주어진 체력 내에서 최대한의 기쁨 느끼기

초기 체력 100, 기쁨 0
만약 체력이 0이나 음수면 죽어서 아무런 기쁨 느끼지 못한 것.
'''
import sys

n = int(input())
L = list(map(int, sys.stdin.readline().split()))
J = list(map(int, sys.stdin.readline().split()))

#0-1 knapsack
#ks[현재까지 만난 사람수][잃은 체력] = 지금까지 얻은 기쁨 최대
ks = [[0 for _ in range(101)] for _ in range(n+1)]

result = 0
for i in range(n):
    for j in range(100):
        #인사 가능
        
        if j + L[i] < 100 :
            #이전 최대 기쁨 + 현재 기쁨
            ks[i][j] = max(ks[i-1][j], ks[i-1][j+L[i]] + J[i])
            
        #인사 불가능
        else:
            ks[i][j] = max(ks[i][j], ks[i-1][j])

        if ks[i][j] > result:
            result = ks[i][j]
            
print(result)

