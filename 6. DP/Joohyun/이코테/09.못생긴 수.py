"""
못생긴 수 :  2,3,5만 소인수로 가지는 수

i 번째가 못생긴 수인 경우
1) i%5 == 0 & i//5 번째 수가 못생긴 수일 경우
2) i%3 == 0 & i//3 번째 수가 못생긴 수일 경우
3) i%2 == 0 & i//2 번째 수가 못생긴 수일 경우

"""
n = int(input())
if n == 1 :
    print(1)
    exit(0)

d = [0]*100000000
d[1],d[2],d[3],d[5] = 1,1,1,1
cnt,i = 1,2
while cnt<n:
    if i%5==0 and d[i//5] :
        d[i]=1
        cnt+=1
    elif i%3==0 and d[i//3]:
        d[i]=1
        cnt+=1
    elif i%2==0 and d[i//2]: 
        d[i]=1
        cnt+=1
    i+=1
print(i-1)
