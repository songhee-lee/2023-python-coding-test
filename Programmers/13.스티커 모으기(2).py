'''
n개의 스티커가 원형으로 연결되어있다.
몇장의 스티커를 뜯어내어 적힌 숫자의 합이 최대가 되도록 하기
단, 한장을 뜯어내면 양쪽으로 인접해있는 스티커는 사용 불가

얻을 수 있는 숫자의 합의 최대값 return
'''

   
# d[i] : 해당 인덱스까지의 최대 점수
# i-1 뜯었는지 안뜯었는지 unknown
def solution(sticker):
    if len(sticker) == 1: 
        return sticker[0]
    
    s = len(sticker)
    
    d1 = [0] * len(sticker)
    d2 = [0] * len(sticker)
    
    d1[0] = sticker[0]
    d1[1] = d1[0]
    for i in range(2, s-1):
        d1[i] = max(sticker[i] + d1[i-2], d1[i-1])
    
    for i in range(1, s):
        d2[i] = max(sticker[i] + d2[i-2], d2[i-1])

    return max(d1[-2], d2[-1])
