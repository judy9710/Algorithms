from heapq import heappush,heappop

def solution(book_time):
    answer = 0
    ans=[]
    book_time.sort(key=lambda x : x[0])
    print(book_time)
    for b in book_time:
        check_in=num(b[0])
        check_out=num(b[1])+10
        if len(ans)!=0 and ans[0]<=check_in: #heap에서 min을 찾는다
            heappop(ans)
        heappush(ans,check_out)
    print(ans)
    answer=len(ans)
    return answer

def num(HHMM):
    HH,MM=HHMM.split(':')
    #print(HH)
    #print(MM)
    return 60*int(HH)+int(MM)
