from collections import defaultdict
p = defaultdict(set)
p[1] = (1,2)
if p : print(f'p = {p}')
else : print('null')
p.pop(1)
if p : print(f'p = {p}')
else : print('null')