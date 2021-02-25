n,m=list(map(int,input().split()))

road_map=[]

for i in range(n):
    road_map.append(list(map(int,input().split())))

houses=[]
chicken=[]

for i in range(n):
    for j in range(n):
        if road_map[i][j]==1:
            houses.append([i,j])
        if road_map[i][j]==2:
            chicken.append([i,j])

# 이 문제는 치킨집 중에서 m 개를 뽑아야 하므로 조합의 개념을 이용한다

from itertools import combinations

candidates=list(combinations(chicken,m)) # 모든 치킨집 중에서 m개의 치킨집을 뽑는 조합 계산

# 치킨 거리의 합을 계산하는 함수

def get_sum(candidate):
    result=0
    for hx,hy in houses:
        # 가장 가까운 치킨집을 찾기
        temp=1e9
        for cx,cy in candidate:
            temp=min(temp,abs(hx-cx)+abs(hy-cy))
        # 가장 가까운 치킨집까지의 거리를 더하기
        result+=temp
    # 치킨 거리의 합 반환
    return result

# 치킨 거리의 합의 최소를 찾아 출력
result=1e9
for candidate in candidates:
    result=min(result,get_sum(candidate))

print(result)
