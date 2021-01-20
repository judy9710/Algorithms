n=int(input())
fear=list(map(int,input().split()))

count=0
fear.sort()#오름차순으로 하면 최소한의 인원으로 그룹 결성, 최대의 수의 그룹 생성 가능
group=0

for i in fear: #낮은 공포도부터 확인하며
    count+=1 #현재 그룹에 해당 모험가를 포함시키기
    if i<=count: #현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        group+=1 # 총 그룹의 수 증가시키기
        count=0 #현재 그룹에 포함된 모험가의 수 초기화      

print(group)

#사람이 일반적으로 조를 짜는 형식과 비슷하게 코딩한 것입
