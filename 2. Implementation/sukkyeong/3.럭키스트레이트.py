n = list(map(int, input()))
answer = len(n) // 2

if sum(n[:answer]) == sum(n[answer:]):
    print('LUCKY')
else:
    print('READY')
