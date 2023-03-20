'''
set함수를 통해
중복을 없애준 후
정렬시킨 새로운 리스트를 만들어 준 후에
arr를 순서대로 돌면서 새로만든 arr2에서 해당 값의 인덱스를 뽑아주기
'''

import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr2 = sorted(list(set(arr)))
dic = {arr2[i]: i for i in range(len(arr2))}
for i in arr:
    print(dic[i], end=' ')
