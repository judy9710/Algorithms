def solution(k, tangerine):
    array=[0]*(max(tangerine)+1)
    for t in tangerine:
        array[t]+=1
    answer = 0
    array.sort()
    if k in array:
        return 1
    for a in array:
        if k<=a:
            return 1
    while (k-array[-1])<=k:
        if len(array)==0 or k==0 or k<0:
            return answer
        k-=array[-1]
        array.pop()
        answer+=1
    return answer

