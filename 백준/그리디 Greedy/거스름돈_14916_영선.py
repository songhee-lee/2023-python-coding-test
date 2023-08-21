#입력 : 거스름돈 액수 n

#출력 : 거스름돈 동전의 최소 개수 출력 못하면 -1

n = int(input())

cnt = 0
flag = 0
while n >= 0:
    if n % 5 == 0 :
        cnt += int(n/5)
        flag = 1
        break
    else:
        cnt += 1
        n -= 2

if flag == 0:
    print(-1)
else:
    print(cnt)
