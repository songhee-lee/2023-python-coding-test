def solution(commands):
    answer = []
    mapp = [["EMPTY"] * 51 for i in range(51)]

    for i in commands:
        #print(i)
        command = i.split(' ')

        if command[0] == 'UPDATE': 
            #글자 업데이트 값이 이미 있는 곳도 가능
            if len(command) == 4:
                r = int(command[1])
                c = int(command[2])
                value = str(command[3])

                if mapp[r][c][0] == "*":
                    temp = mapp[r][c].split(' ')
                    mapp[int(temp[1])][int(temp[2])] = value
                else:
                    mapp[r][c] = value

            #글자 찾아 바꾸기
            elif len(command) == 3:
                for j in range(51):
                    for k in range(51):
                        if mapp[j][k] == command[1]:
                            mapp[j][k] = str(command[2])

        #병합
        #value가 숫자인 경우만 있을수도 잇어서 string으로 판단하면 안됨
        if command[0] == 'MERGE':
            r1 = int(command[1])
            c1 = int(command[2])
            r2 = int(command[3])
            c2 = int(command[4])
            if r1 == r2 and c1 == c2:
                continue

            #두 셀 모두 값을 가지고 있을 경우 병합된 셀은 (r1, c1) 위치의 셀 값을 가지게 됩니다
            #두 셀 중 한 셀만 값을 가지고 있을 경우
            if mapp[r1][c1] != "EMPTY" and mapp[r1][c1][0] != "*" and mapp[r2][c2] == "EMPTY":
                mapp[r2][c2] = "* " + command[1] + " " + command[2] 
            elif mapp[r2][c2] != "EMPTY" and mapp[r2][c2][0] != "*" and mapp[r1][c1] == "EMPTY":
                mapp[r1][c1] = "* " + command[3] + " " + command[4]
            #두 셀 모두 값을 가지고 있는 경우
            elif mapp[r1][c1] != "EMPTY" and mapp[r2][c2] != "EMPTY" and mapp[r1][c1][0] != "*" and mapp[r2][c2][0] != "*":
                mapp[r2][c2] = "* " + command[1] + " " + command[2]                                                    
            #두 셀 중 한 셀이 머지 되어 있는 경우
            elif mapp[r1][c1][0] == "*" and mapp[r2][c2][0] != "*":
                if r2 == int(mapp[r1][c1][2]) and c2 == int(mapp[r1][c1][4]):
                    continue
                mapp[r2][c2] = mapp[r1][c1]
            elif mapp[r2][c2][0] == "*" and mapp[r1][c1][0] != "*":
                if r1 == int(mapp[r2][c2][2]) and c1 == int(mapp[r2][c2][4]):
                    continue
                mapp[r1][c1] = mapp[r2][c2]
            #두 셀 모두 머지 되어 있는 경우
            elif mapp[r1][c1][0] == "*" and mapp[r2][c2][0] == "*":
                for j in range(51):
                    for k in range(51):
                        if mapp[j][k] == mapp[r2][c2]:
                            mapp[j][k] = mapp[r1][c1] 
            #mapp[r2][c2] = "* " + command[1] + " " + command[2]
    
        #병합 해제
        if command[0] == 'UNMERGE':
            r = int(command[1])
            c = int(command[2])
            r1, c1 = r, c
            if mapp[r][c][0] == "*":
                while(mapp[r][c][0] == '*'):
                    temp = mapp[r][c].split(' ')
                    mapp[r][c] = "EMPTY"
                    r = int(temp[1])
                    c = int(temp[2])
                mapp[r1][c1] = mapp[r][c]
                mapp[r][c] = "EMPTY" 
            else:
                for j in range(51):
                    for k in range(51):
                        if mapp[j][k][0] == "*":
                            temp = mapp[j][k].split(' ')
                            t_r = int(temp[1])
                            t_c = int(temp[2])
                            if r1 == t_r and c1 == t_c:
                                mapp[j][k] = "EMPTY"
                

                    
        
        if command[0] =='PRINT':
            r = int(command[1])
            c = int(command[2])
            if mapp[r][c][0] == "*":
                while(mapp[r][c][0] == '*'):
                    temp = mapp[r][c].split(' ')
                    r = int(temp[1])
                    c = int(temp[2])
                answer.append(mapp[r][c])
            else:
                answer.append(mapp[r][c])

       #printing(mapp)            
    #print(answer)
    return answer



'''
#1,3,4,5,7,8,10,12,21 통과
def solution(commands):
    answer = []
    mapp = [["EMPTY"] * 51 for i in range(51)]
    merge = []
    merge_cnt = 0
    max_n = -1
    for i in commands:
        temp = i.split(' ')

        if temp[0] == 'UPDATE': 
            #글자 업데이트
            if len(temp) == 4:
                if max_n < int(temp[1]):
                    max_n = int(temp[1])
                elif max_n < int(temp[2]):
                    max_n = int(temp[2])
                #map의 값이 숫자일 경우 merge 되어 있는 것.
                if mapp[int(temp[1])][int(temp[2])][0] == "*":
                    merge[int(mapp[int(temp[1])][int(temp[2])][1])] = str(temp[3])
                #아니면 평범하게 update
                else:
                    mapp[int(temp[1])][int(temp[2])] = str(temp[3])
                #print("UPDATE",temp[1], temp[2])
                #print(mapp[int(temp[1])][int(temp[2])])

            #글자 찾아 바꾸기
            elif len(temp) == 3:
                for j in range(51):
                    for k in range(51):
                        if mapp[j][k] == temp[1]:
                            mapp[j][k] = str(temp[2])
                            #print("UPDATE", temp[1], "to", temp[2])
                            #print(j,k)

        #연결되있는 걸 표시
        #병합할 두 셀 모두 값이 없는 경우?
        if temp[0] == 'MERGE':
            if mapp[int(temp[1])][int(temp[2])][0] == "*":
                mapp[int(temp[3])][int(temp[4])] = mapp[int(temp[1])][int(temp[2])]
            else:
                merge.append(mapp[int(temp[1])][int(temp[2])])
                mapp[int(temp[1])][int(temp[2])] = "*" + str(merge_cnt)
                mapp[int(temp[3])][int(temp[4])] = "*" + str(merge_cnt)
                merge_cnt +=1
                #print("merge", merge, temp[1],temp[2])
                #print("mapp", mapp[int(temp[1])][int(temp[2])])
                #print("merge_cnt", merge_cnt)
    
        #셀 병합 해제 후 원래 값은 temp1,tmpe2가 가짐 (나머지는 빈칸)
        if temp[0] == 'UNMERGE':
            if mapp[int(temp[1])][int(temp[2])][0] != "*":
                continue 
            num = mapp[int(temp[1])][int(temp[2])]
            mapp[int(temp[1])][int(temp[2])] = merge[int(num[1:])]
            
            for j in range(51):
                for k in range(51):
                    if mapp[j][k] == num:
                        mapp[j][k] = "EMPTY"
                    
        
        if temp[0] =='PRINT':
            if mapp[int(temp[1])][int(temp[2])][0] == "*":
                #print(mapp[int(temp[1])][int(temp[2])])
                answer.append(merge[int(mapp[int(temp[1])][int(temp[2])][1])])
            else:
                answer.append(mapp[int(temp[1])][int(temp[2])])
    #print(answer)
    return answer



#1,3,4,5,8,21,22 통과
def solution(commands):
    answer = []
    mapp = [["EMPTY"] * 51 for i in range(51)]
    merge = []
    merge_cnt = 0
    max_n = -1
    for i in commands:
        temp = i.split(' ')

        if temp[0] == 'UPDATE': 
            #글자 업데이트
            if len(temp) == 4:
                if max_n < int(temp[1]):
                    max_n = int(temp[1])
                elif max_n < int(temp[2]):
                    max_n = int(temp[2])
                #map의 값이 숫자일 경우 merge 되어 있는 것.
                if mapp[int(temp[1])][int(temp[2])].isdigit():
                    merge[int(mapp[int(temp[1])][int(temp[2])])] = str(temp[3])
                #아니면 평범하게 update
                else:
                    mapp[int(temp[1])][int(temp[2])] = str(temp[3])
                #print("UPDATE",temp[1], temp[2])
                #print(mapp[int(temp[1])][int(temp[2])])

            #글자 찾아 바꾸기
            elif len(temp) == 3:
                for j in range(51):
                    for k in range(51):
                        if mapp[j][k] == temp[1]:
                            mapp[j][k] = str(temp[2])
                            #print("UPDATE", temp[1], "to", temp[2])
                            #print(j,k)

        #연결되있는 걸 표시
        #병합할 두 셀 모두 값이 없는 경우?
        if temp[0] == 'MERGE':
            if mapp[int(temp[1])][int(temp[2])].isdigit():
                mapp[int(temp[3])][int(temp[4])] = mapp[int(temp[1])][int(temp[2])]
            else:
                merge.append(mapp[int(temp[1])][int(temp[2])])
                mapp[int(temp[1])][int(temp[2])] = str(merge_cnt)
                mapp[int(temp[3])][int(temp[4])] = str(merge_cnt)
                merge_cnt +=1
                #print("merge", merge, temp[1],temp[2])
                #print("mapp", mapp[int(temp[1])][int(temp[2])])
                #print("merge_cnt", merge_cnt)
    
        #셀 병합 해제 후 원래 값은 temp1,tmpe2가 가짐 (나머지는 빈칸)
        if temp[0] == 'UNMERGE':
            num = mapp[int(temp[1])][int(temp[2])]
            mapp[int(temp[1])][int(temp[2])] = merge[int(num)]
            
            for j in range(51):
                for k in range(51):
                    if mapp[j][k] == num:
                        mapp[j][k] = "EMPTY"
                    
        
        if temp[0] =='PRINT':
            if mapp[int(temp[1])][int(temp[2])].isdigit():
                answer.append(merge[int(mapp[int(temp[1])][int(temp[2])])])
            else:
                answer.append(mapp[int(temp[1])][int(temp[2])])
        
    return answer

3,4,5 통과
def solution(commands):
    answer = []
    mapp = [["EMPTY"] * 51 for i in range(51)]
    merge = []
    merge_cnt = 0
    max_n = -1
    for i in commands:
        temp = i.split(' ')

        if temp[0] == 'UPDATE': 
            #글자 업데이트
            if len(temp) == 4:
                if max_n < int(temp[1]):
                    max_n = int(temp[1])
                elif max_n < int(temp[2]):
                    max_n = int(temp[2])
                #map의 값이 숫자일 경우 merge 되어 있는 것.
                if mapp[int(temp[1])][int(temp[2])][0] == "*":
                    merge[int(mapp[int(temp[1])][int(temp[2])])] = str(temp[3])
                #아니면 평범하게 update
                else:
                    mapp[int(temp[1])][int(temp[2])] = str(temp[3])
                #print("UPDATE",temp[1], temp[2])
                #print(mapp[int(temp[1])][int(temp[2])])

            #글자 찾아 바꾸기
            elif len(temp) == 3:
                for j in range(51):
                    for k in range(51):
                        if mapp[j][k] == temp[1]:
                            mapp[j][k] = str(temp[2])
                            #print("UPDATE", temp[1], "to", temp[2])
                            #print(j,k)

        #연결되있는 걸 표시
        #병합할 두 셀 모두 값이 없는 경우?
        if temp[0] == 'MERGE':
            if mapp[int(temp[1])][int(temp[2])][0] == "*":
                mapp[int(temp[3])][int(temp[4])] = mapp[int(temp[1])][int(temp[2])]
            else:
                merge.append(mapp[int(temp[1])][int(temp[2])])
                mapp[int(temp[1])][int(temp[2])] = "*" + str(merge_cnt)
                mapp[int(temp[3])][int(temp[4])] = "*" + str(merge_cnt)
                merge_cnt +=1
                #print("merge", merge, temp[1],temp[2])
                #print("mapp", mapp[int(temp[1])][int(temp[2])])
                #print("merge_cnt", merge_cnt)
    
        #셀 병합 해제 후 원래 값은 temp1,tmpe2가 가짐 (나머지는 빈칸)
        if temp[0] == 'UNMERGE':
            num = mapp[int(temp[1])][int(temp[2])]
            mapp[int(temp[1])][int(temp[2])] = merge[int(num[1:])]
            
            for j in range(51):
                for k in range(51):
                    if mapp[j][k] == num:
                        mapp[j][k] = "EMPTY"
                    
        
        if temp[0] =='PRINT':
            if mapp[int(temp[1])][int(temp[2])][0] == "*":
                #print(mapp[int(temp[1])][int(temp[2])])
                answer.append(merge[int(mapp[int(temp[1])][int(temp[2])][1])])
            else:
                answer.append(mapp[int(temp[1])][int(temp[2])])
    #print(answer)
    return answer
'''
