n = int(input())
d = [0]*(n+1) # 대칭 고려 x
s = [0]*(n+1) # 대칭
d[1],d[2] = 1,3
s[1],s[2],s[3],s[4] = 1,3,1,5

for i in range(3,n+1):
  d[i] = 2*d[i-2]+d[i-1]
for i in range(5,n+1):
  s[i] = s[i-2]+2*s[i-4] 

print((d[n]-s[n])//2 + s[n])