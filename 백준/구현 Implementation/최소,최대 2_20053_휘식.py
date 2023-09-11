t = int(input())
for _ in range(t):
  n = int(input())
  _min, _max = 1000001, -1000001
  for i in map(int, input().split()):
    if _min > i:
      _min = i
    if _max < i:
      _max = i
  print(_min, _max)