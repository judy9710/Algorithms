from collections import deque
def solution(priorities, location):
    answer = 0
    q=deque(priorities)
    #print(q)
    new_q=deque()
    # 큐 자료구조를 그대로 구현
    # 원형 큐 개념임
    for idx, value in enumerate(q):
        new_q.append([idx,value])
    print(new_q)
    array=[]
    while new_q:
        flag=False
        a=new_q.popleft()
        #print(a)
        for i in range(len(new_q)):
            if new_q[i][1]>a[1]:
                flag=True
                break
        if flag==True:
            new_q.append(a) #다시 큐에 집어넣는다
        elif flag==False:
            array.append(a[0]) # 실행한 프로세스를 저장하는 배열임
            if a[0]==location:
                break
    print(array)
    answer=len(array)
    return answer
