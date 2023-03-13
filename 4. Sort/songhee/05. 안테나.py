""" 
- 안테나와 모든 집까지의 거리의 총합이 최소가 되도록 설치
- 안테나는 집 위치에만 설치 가능
- 집 위치는 중복이 가능함

- 안테나 위치 여러 개일 경우 작은 값 출력
"""
import sys

N = int(input())
house = list(map(int, sys.stdin.readline().split()))

print(sorted(house)[ (N-1) // 2])
