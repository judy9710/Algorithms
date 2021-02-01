def solution(food_times,k):
    count=0
    eat=0
    while eat!=k:
        if count>len(food_times)-1:
            count=0
        if food_times[count]>0:
            food_times[count]-=1
            count+=1
            eat+=1
        elif food_times[count]==0:
            count+=1
    if count>len(food_times)-1:
        count=0
    answer=count+1
    return answer

food_times=list(map(int,input().split()))
k=int(input())

print(solution(food_times,k))
