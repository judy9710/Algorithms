def solution(n):
    answer = 0
    for i in range(1,n//2+1):
        accum=0
        while accum<n:
            accum+=(i)
            i+=1
        if accum==n:
            answer+=1
    answer+=1    
    return answer
