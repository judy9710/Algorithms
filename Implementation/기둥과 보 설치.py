#import heapq

def solution(n, build_frame):
    #answer=[[]*(n) for i in range(n)]
    answer=[]
    for i in build_frame:
        if i[2]==0 and i[3]==1: #기둥을 설치하라고 하면
            if i[1]==0 or ([i[0],i[1],1] in answer) or ([i[0]-1,i[1],1] in answer) or ([i[0],i[1]-1,0] in answer):
                answer.append([i[0],i[1],i[2]])
        elif i[2]==1 and i[3]==1:#보를 설치하라고 하면
            if ([i[0],i[1]-1,0] in answer) or ([i[0]+1,i[1]-1,0] in answer) or (([i[0]-1,i[1],1] and [i[0]+1,i[1],1]) in answer):
                answer.append([i[0],i[1],i[2]])
        elif (i[2]==0 or i[2]==1) and i[3]==0: #기둥과 보를 삭제하라고 하면
            temp=[i[0],i[1],i[2]]
            answer.remove(temp) #우선 삭제를 해보고
            for i in answer:
                if i[2]==0: #남아있는거 중에서 기둥이라면
                    if i[1]==0 or ([i[0],i[1],1] in answer) or ([i[0]-1,i[1],1] in answer) or ([i[0],i[1]-1,0] in answer):
                    # 기둥이 땅위에 있거나 보가 연결되어있거나 조건을 만족시키면
                        continue
                    else: #조건을 만족시키지 못하면
                        answer.append(temp) #다시 붙인다
                elif i[2]==1: #남아있는거 중에서 보라면
                    if ([i[0]+1,i[1]-1,0] in answer) or ([i[0],i[1]-1,0] in answer) or (([i[0]+1,i[1],1] and [i[0]-1,i[1],1]) in answer):
                        continue # 보가 양쪽이 보와 연결되어있거나 혹은 보의 한쪽 끝부분이 기둥 위에 있는 경우
                    else: #조건을 만족시키지 못하면
                        answer.append(temp)
    return answer


#build_frame=[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
build_frame=[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]


answer=solution(5,build_frame)
answer.sort()
print(answer)
