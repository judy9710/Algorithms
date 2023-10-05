import heapq
def solution(scoville, K):
    answer=0
    heapq.heapify(scoville)
    while(True):
        if len(scoville)==1:
            if scoville[0]<K:
                answer=-1
            else:
                answer=answer
            return answer
        first=heapq.heappop(scoville)
        second=heapq.heappop(scoville)
        if first<K or second<K:
            new=first+(2*second)
            heapq.heappush(scoville,new)
            answer+=1
        elif first>=K and second>=K:
            return answer
