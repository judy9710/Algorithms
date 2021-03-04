from itertools import permutations

def solution(n, weak, dist):
    # 이 문제의 핵심은 원형 나열되 데이터 -> 일자로 만드는 작업
    length=len(weak)
    for i in range(length):
        weak.append(weak[i]+n)
    answer=len(dist)+1 # 나중에 min 함수로 최소값을 찾아야하므로 len(dist)+1로 초기화
    # 0부터 n-1 까지의 위치를 각각 시작점으로 설정
    for start in range(length):
        # 친구를 나열하는 모든 경우의 수 각각에 대하여 확인
        for friends in list(permutations(dist,len(dist))):
            count=1 #투입할 친구의 수
            # 해당 친구가 점검할 수 있는 마지막 위치
            position=weak[start]+friends[count-1]
            # 시작점부터 모든 취약 지점을 확인
            for index in range(start,start+length):
                # 점검할 수 있는 위치를 벗어난 경우
                if position<weak[index]:
                    count+=1 #새로운 친구를 투입
                    if count>len(dist):
                        break
                    position=weak[index]+friends[count-1]
            answer=min(answer,count)
    if answer>len(dist):
        return -1
    return answer
