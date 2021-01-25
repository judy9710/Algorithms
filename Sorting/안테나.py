n=int(input())
home_positions=list(map(int,input().split()))

tracking=[]

for h in home_positions:
    position=h
    result2=0
    for i in home_positions:
        distance=i-h
        if distance<0:
            distance=distance*(-1)
        result2+=distance
    tracking.append((result2,position))

tracking.sort(key=lambda x:(x[0],x[1]))

print(tracking[0][1])

# 근데 이 문제는 단순히 중간값을 출력하는 문제로 단순화될 수 있다
