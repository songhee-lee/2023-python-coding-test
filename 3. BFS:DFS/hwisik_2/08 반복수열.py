'''
✅ 기저조건 설정 : 언제부터 반복수열이 되는가? -> 언제 반복문을 종료해야 하는가?

- '반복되는 부분을 제외한 수열'과 '반복되는 부분만 저장하는 수열'을 선언한다.
- 반복되는 부분이 나오기 전까지, 모든 수열을 '반복되는 부분을 제외한 수열'에 저장한다.
- 반복되는 부분이 나온다면, 해당 수열을 '반복되는 부분만 저장하는 수열'에 저장한다.
- 최종적으로 '반복되는 부분을 제외한 수열' - '반복되는 부분만 저장하는 수열' 이 답이 된다.(차집합?)
'''
import sys
a, p = map(int, sys.stdin.readline().split())

perm_set = set()
duplicate_set = set()
perm_set.add(a)

cur_num = a

def make_next_num(num):
    new_num = 0
    while num:
        new_num += (num % 10) ** p
        num //= 10
        
    return new_num

while True:
    new_num = make_next_num(cur_num)
    if new_num in perm_set:
        while new_num not in duplicate_set:    
            duplicate_set.add(new_num)
            new_num = make_next_num(new_num)
        break
    else: 
        perm_set.add(new_num)
    cur_num = new_num
    
out = perm_set - duplicate_set
print(len(out))