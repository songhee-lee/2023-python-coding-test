'''
w1 : c = w : h2, w2 : c = w : h1라는 점을 통해

w1 = c*w / h2, w2 = c*w / h1

w = w1 + w2 = c*w / h2 + c*w / h1 = c*w*(h1+h2) / (h1*h2)

-> 1 = c*(h1+h2) / (h1*h2) -> c = h1*h2 / (h1+h2)

h1 = (x**2-w**2)**0.5, h2 = (y**2-w**2)**0.5
'''


def f(x, y, w):
    h1 = (x**2-w**2)**0.5
    h2 = (y**2-w**2)**0.5
    c = h1*h2 / (h1+h2)
    return c


x, y, c = map(float, input().split())
s, e = 0, min(x, y)
res = 0
while e-s > 0.000001:
    m = (s+e)/2
    if f(x, y, m) >= c:
        res = m
        s = m
    else:
        e = m
print(res)
