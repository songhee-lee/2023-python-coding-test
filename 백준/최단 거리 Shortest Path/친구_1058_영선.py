#입력1: 사람수 n
#입력2(n개의 줄): 친구면y 아니면 n

#출력 : 가장 유명한 사람의 2-친구의 수 출력

'''
가장 유명한 사람 = 2-친구의 수가 가장 많은 사람
2-친구 ? A와 B가 친구거나 A와B 사이의 C 가 존재하면 둘은 2-친
'''

import sys

n = int(input())
friend = [sys.stdin.readline().rstrip() for _ in range(n)]

two = [[0]* n for _ in range(n)]

#서로 친구면 거리 1
#한다리 건너면 거리 2

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j :
                continue

            if friend[i][j] =='Y' or (friend[i][k] == 'Y' and friend[k][j] =='Y'):
                two[i][j] = 1

ans = 0
for t in two:
    ans = max(ans, sum(t))

print(ans)
