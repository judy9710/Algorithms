# length라는 변수를 따로 두어서 그것에 count를 하나씩 빼는 방법 사용

def solution(N,stages):
    answer=[]
    length=len(stages)

    for i in range(1,N+1):
        count=stages.count(i)

        if length==0:
            fail=0 # 스테이지에 도달한 유저수가 없으면 해당 스테이지의 실패율=0

        else:
            fail=count/length

        answer.append((i,fail))
        length-=count

    answer=sorted(answer,key=lambda x:x[1], reverse=True) #내림차순이므로
    # 실패율을 기준으로 각 스테이지를 내림차순 정렬

    answer=[i[0] for i in answer] # list comprehension 방법으로 스테이지 출력
    return answer

N=int(input())
stages=list(map(int,input().split()))

result=solution(N,stages)
print(result)
