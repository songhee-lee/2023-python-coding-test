def solution(n, info):
    answer = [0] * 11
    arr = [0] * 11      # 라이언이 쏜 화살 개수
    maxDiff = 0
    
    # 1이면 피치+1 개로 점수 획득한다고 할 때,
    # 000..0 ~ 111..1 까지 확인
    for subset in range(1, 1 << 10):
        ryan, peach = 0, 0  # 라이언, 피치 점수
        cnt = 0             # 과녁에 쏜 화살 개수
        
        for i in range(10):
            # 라이언이 점수를 획득한다면
            if subset & (1 << i):
                ryan += 10-i
                arr[i] = info[i]+1
                cnt += arr[i]
            # 아니라면
            else:
                arr[i] = 0
                if info[i]:     # 피치가 화살 쏜 경우
                    peach += 10-i
                    
        if cnt > n : continue   # 화살을 더 많이 날린 경우 
        arr[10] = n - cnt       # 남은 화살 있으면 0점에 넣기
        
        # 점수 차이가 많이 나는 화살셋으로 변경
        if ryan - peach > maxDiff:
            maxDiff = ryan - peach
            answer = arr[:]
        # 점수 차 같다면 가장 낮은 점수를 많이 맞춘 경우인지 확인
        elif ryan - peach == maxDiff:
            for j in reversed(range(11)):
                if arr[j] > answer[j]:
                    maxDiff = ryan-peach
                    answer = arr[:]
                    break
                elif arr[j] < answer[j]:
                    break
    
    # 라이언이 이기는 경우가 없는 경우
    if maxDiff == 0:
        answer = [-1]
            
    return answer