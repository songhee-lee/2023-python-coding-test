""" 
- A 빌딩의 x 사다리, B 빌딩의 y 사다리는 c 지점에서 교차한다
- 두 빌딩은 얼마나 떨어져 있을까?
"""
x, y, c = map(float, input().split())

s, e = 0, min(x, y)
ans = 0
while e-s > 0.000001 :
    m = (s+e) / 2

    h1 = (x**2 - m**2)**0.5
    h2 = (y**2 - m**2)**0.5
    cant = h1*h2 / (h1+h2)
    
    if cant >= c:
        ans = m
        s = m
    else:
        e = m

print(ans)