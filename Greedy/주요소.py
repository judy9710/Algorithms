# 백준 13305번
# 주요소 (실버3)

# 서브 태스크 1 - 모든 주유소의 1리터당 가격이 1원인 경우

N=int(input())
weight=list(map(int,input().split()))
cost=list(map(int,input().split()))

#print(sum(weight))

# 서브 태스크 2,3
# 그리디 알고리즘은 그때그때 가장 좋은 선택을 하는 것임
# 하나씩 돌아가면서 그때 남아있는 것들 중 가장 작은 cost
min=1000000000
total_cost=0
for i in range(len(weight)):
    if min>cost[i]:
        min=cost[i]
    total_cost+=(min*weight[i])
print(total_cost)
