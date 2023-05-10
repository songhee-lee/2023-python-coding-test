'''
모든 집까지 거래의 총합 최소
'''
n = int(input())
house = []
house = list(map(int, input().rstrip().split()))
house.sort()
print(house[(n-1)//2])
