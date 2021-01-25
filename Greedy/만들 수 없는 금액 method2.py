# 단순히 동전을 화폐 단위 기준으로 정렬한 뒤에, 화폐 단위가 작은
# 동전부터 하나씩 확인하면서 target 변수를 업데이트하는 방법으로
# 최적의 해를 계산할 수 있다

n=int(input())
data=list(map(int,input().split()))
data.sort()

target=1
for x in data:
    # 만들 수 없는 금액을 찾았을 때 종료
    if target<x:
        break
    target+=x

print(target)

# 유명한 그리디 문제를 푸는 방법중 하나
