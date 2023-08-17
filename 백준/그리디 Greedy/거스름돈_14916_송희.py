N = int(input())

if N == 1 or N == 3 :
    print(-1)
else :
    five = N // 5
    two = (N % 5) // 2
    
    print(five + two) if (N % 5) % 2 == 0 else print(five-1 +two+3)