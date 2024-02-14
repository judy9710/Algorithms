from collections import deque
import copy

def solution(bridge_length, weight, truck_weights):
    answer = 0
    # 딱 보면 스택 혹은 큐 자료구조 이용하는 문제임
    # 1초에 1씩 갈 수 있는 것 같다
    
    passed=[] # 다리를 지난 트럭
    passing=deque() # 다리를 건너는 트럭
    waiting=deque(truck_weights) # 대기 트럭
    time={}
    for i in truck_weights:
        time[i]=bridge_length
    
    passing.append(waiting.popleft()) #1초에 첫 트럭이 지나감
    answer+=1 # 1초 시작
    time[passing[0]]-=1 # 1초 감소시킴
    
    while passing:
        for i in copy.deepcopy(passing):
            if time[i]==0:
                passed.append(passing.popleft())
        if len(passing)<bridge_length:
            if len(waiting)!=0:
                passing.append(waiting.popleft())
            if sum(passing)>weight:
                a=passing.pop()
                waiting.appendleft(a)
                for i in copy.deepcopy(passing):
                    time[i]-=1
                answer+=1
                continue
            else:
                for i in copy.deepcopy(passing):
                    time[i]-=1
                answer+=1
                continue
                    
            
    return answer
