# 에어컨 킨 동안: 실내온도 -> 희망온도(임의 설정)
# 에어컨 끈 동안: 실내온도 -> 실외온도(실내온도와 실외온도가 같다면 실내온도는 변하지 않는다.)
# 소비전력 -> 실내온도에 따라 달라짐 / 희망온도 == 실내온도 ? 매 분 전력을 b 만큼 소비 : a 만큼 소비
# 에어컨 끈 동안: 전력 소비 X
# 승객이 탑승 중일 때 실내온도를 t1 ~ t2도 사이로 유지
# 희망온도를 내가 임의로 설정하여 최소 소비전력을 구해야 한다.

''' ref
희망온도를 몇도로 설정할 것인가?
에어컨을 언제 끌 것인가?
✅ 실내온도 <= t1 : 희망온도 >= t1
✅ 실내온도 >= t2 : 희망온도 <= t2
'''
def solution(temperature, t1, t2, a, b, onboard):
    k = 1000 * 100
    t1 += 10
    t2 += 10
    temperature += 10
    
    # DP[i][j] : i분에 j 온도를 만들 수 있는 가장 적은 전력
    DP = [[k] * 51 for _ in range(len(onboard))] # j = 0 : -10 // = 50 : 40
    DP[0][temperature] = 0
    
    flag = 1 # 에어컨을 가동했을때 온도가 변하는 방향
    if temperature > t2 :
        flag = -1
    for i in range(1, len(onboard)):
        for j in range(51):
            arr = [k]
            if (onboard[i] == 1 and t1 <= j <= t2) or onboard[i] == 0:
                # 1. 에어컨을 키지 않고 실외온도와 달라서 실내온도가 -flag 되는 경우
                if 0 <= j+flag <= 50 :
                    arr.append(DP[i-1][j+flag])
                # 2. 에어컨을 키지 않고 현재온도 j 가 실외온도랑 같아서 변하지 않는 경우
                if j == temperature:
                    arr.append(DP[i-1][j])
                # 3. 에어컨을 키고 현재온도가 변하는 경우
                if 0 <= j-flag <= 50:
                    arr.append(DP[i-1][j-flag] + a)
                # 4. 에어컨을 키고 현재온도가 희망온도라서 온도가 변하지 않는경우
                if t1 <= j <= t2:
                    arr.append(DP[i-1][j] + b)

                DP[i][j] = min(arr)
            
    answer = min(DP[len(onboard)-1])
    return answer