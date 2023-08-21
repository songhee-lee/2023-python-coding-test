# 무조건 5원짜리로 가능한 만큼 거슬러 주면 안된다.
# 13원일 때 예외가 발생. -> 5원 + 5원 + 3원이 되는데, 3원은 2원으로도 해결이 안된다.

n = int(input())

count = 0
while True:
  if n == 0 or n < 2 : break
  if n % 5 == 0:
    count += n // 5
    n %= 5
  else:
    count += 1
    n -= 2

if n != 0: print(-1)
else: print(count)