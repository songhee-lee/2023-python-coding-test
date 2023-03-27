'''
d[0][0]=7
d[1][0]=3+7,
d[1][1]=8+7
d[2][0]=8+d[1][0],
d[2][1]=1+max(d[1][0],d[1][1]),
d[2][2]=0+d[1][1]


'''

n = int(input())
d = []
for i in range(n):
    d.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(len(d[i])):
        if j == 0:
            d[i][j] = d[i][j]+d[i-1][j]
        elif j == len(d[i])-1:
            d[i][j] = d[i][j]+d[i-1][j-1]
        else:
            d[i][j] = max(d[i-1][j-1], d[i-1][j])+d[i][j]
print(max(d[n-1]))
