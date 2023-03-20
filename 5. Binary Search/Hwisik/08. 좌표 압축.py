'''
- Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표의 개수와 같아야 한다.

- 같은 위치의 좌표는 좌표 압축 후에도 같은 위치를 가져야 한다. -> 중복되는 원소를 제거해야 한다.
- 중복을 제거하기 위해 set 사용
    - 입력받은 리스트를 set으로 중복 제거 후, 
        다시 list로 만든 후 정렬한 결과를 새로운 리스트에 저장한다.
- 정렬된 리스트를 (key : 원소, value : 인덱스) 형태인 딕셔너리로 저장한다.
- 출력한다.
'''

import sys

n = int(sys.stdin.readline())
coords = list(map(int, sys.stdin.readline().split())) # 입력받은 리스트
new_coords = sorted(list(set(coords))) # 중복 제거한 리스트

# (key : 원소, value : 인덱스) 형태인 딕셔너리
dic = {new_coords[i] : i for i in range(len(new_coords))}

# 해당 원소의 위치 출력
for coord in coords:
    print(dic[coord], end=' ')