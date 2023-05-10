# 풀이 참조
n = list(map(int,input()))
l = len(n)
d = [0 for _ in range(l+1)]
if n[0]==0 : print("0")
else:
    n=[0]+n
    d[0]=d[1]=1
    for i in range(2,l+1):
        if n[i]:            # 현재 위치의 암호가 0이 아닐 경우 이전 dp 값을 더해준다
            d[i]+=d[i-1]
        tmp = n[i-1]*10+n[i]    # 이전 암호랑 현재 암호를 하나의 숫자로
        if tmp >= 10 and tmp <= 26:
            d[i]+=d[i-2]
    print(d[l]%1000000)
        