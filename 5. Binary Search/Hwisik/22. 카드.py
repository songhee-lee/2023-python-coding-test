'''
- 카드의 숫자 : Key, 가지고 있는 개수 : Value인 Dictionary 사용.
- 입력에 따라, 딕셔너리를 만든다.
- Value를 기준으로 내림차순 정렬하고, 같다면 Key를 기준으로 오름차순 정렬한다.
'''
import sys
from collections import defaultdict

n = int(sys.stdin.readline())
dic = defaultdict(int) # 딕셔너리

for _ in range(n):
    card = int(sys.stdin.readline())
    dic[card] += 1

# '가지고 있는 개수' 기준 내림차순, 
# '카드에 쓰여진 수' 기준 오름차순,
ret = sorted(dic.items(), key=lambda x: (-x[1], x[0]))

# 출력
print(ret[0][0])