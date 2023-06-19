# HH:MM:SS를 '초'로 변환
def format_time(time):
    h, m, s = map(int, time.split(":"))
    return h * 3600 + m * 60 + s

# '초'를 HH:MM:SS로 변환
def deformat_time(time):
    m, s = divmod(time, 60)
    h, m = divmod(m, 60)
    return '{:02d}:{:02d}:{:02d}'.format(h, m, s)

def solution(play_time, adv_time, logs):
    play_time = format_time(play_time) # 전체 동영상 재생시간
    adv_time = format_time(adv_time) # 광고 재생시간
    
    dp = [0] * (play_time + 1) # DP 배열
    
    # [시작 시간, 종료 시간]에서의 재생중인 시청자 수 기록
    for log in logs:
        s, e = log.split("-")
        s, e = format_time(s), format_time(e)
        
        dp[s] += 1
        dp[e] -= 1
    
    # 구간 별 시청자수 기록
    for i in range(1, play_time + 1):
        dp[i] += dp[i - 1]
    
    # 모든 구간 시청자수 누적 합(기록)
    for i in range(1, play_time + 1):
        dp[i] += dp[i - 1]
            
    start_time = 0 # 광고가 들어갈 시작 시각
    max_view = dp[adv_time] # 최대 시청자 수
    
    # 최대 시청자 수 찾기
    for i in range(adv_time, play_time + 1):
        # 현재 구간의 시청자 수가 최대 시청자 수 보다 많다면
        if max_view < dp[i] - dp[i - adv_time]:
            max_view = dp[i] - dp[i - adv_time]
            start_time = i - adv_time + 1 # 시작 시각 갱신
    
    # HH:MM:SS로 변환하여 반환
    return deformat_time(start_time)