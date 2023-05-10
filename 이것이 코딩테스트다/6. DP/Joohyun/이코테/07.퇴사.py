# 답지 참고

n=int(input())
t,p = [],[]
d = [0]*(n+1)
max_value = 0

for _ in range(n):
    x,y=map(int,input().split())
    t.append(x)
    p.append(y)

# 리스트를 뒤에서부터 거꾸로 확인
for i in range(n-1,-1,-1):
    time = t[i]+i

    # 상담이 기간 안에 끝나는 경우
    if time <= n:
        d[i]=max(p[i]+d[time], max_value)
        max_value=d[i]

    # 상담이 기간을 벗어나는 경우
    else: d[i] = max_value

print(max_value)