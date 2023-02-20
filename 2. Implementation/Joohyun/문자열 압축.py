def solution(s):
    answer = s
    for i in range(len(s)//2):
        unit = i+1
        standard = s[0:unit]
        from_s, to_s = unit, unit*2
        nowList,same = [],1
        
        while True:
            if standard == s[from_s:to_s] : same+=1
            else : 
                if same==1 : nowList.append(standard)
                else:
                    nowList.append('{0}{1}'.format(str(same),standard))
                    same=1
                standard=s[from_s:to_s]

            from_s+=unit
            to_s+=unit
            
            if to_s > len(s):
                if same==1 : nowList.append(standard)
                else : nowList.append('{0}{1}'.format(str(same),standard))
                nowList.append(s[from_s:])
                nowStr=''.join(nowList)
                break
            
        if len(nowStr)<len(answer):
            answer=nowSt
    return len(answer)