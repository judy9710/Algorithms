def solution(N, stages):
    answer = []
    for j in range(1,N+1):
        bottom=0
        up=0
        for i in stages:
            if i>=j:
                bottom+=1
            if i==j:
                up+=1
        failure_rate=float(up)/float(bottom)
        answer.append((failure_rate,j))
        #print(failure_rate)
    return answer

N=int(input())
stages=list(map(int,input().split()))

result=solution(N,stages)

result.sort(reverse=True, key=lambda x:(float(x[0])))

print([i[1] for i in result])
