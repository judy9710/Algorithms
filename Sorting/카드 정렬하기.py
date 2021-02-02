# 이 문제는 오름차순으로 우선 정렬하고 첫번째부터 마지막까지 곱해가며 더하기

n=int(input())
cards=[]

for _ in range(n):
    k=int(input())
    cards.append(k)

cards.sort()
sum=0

for i in range(1,len(cards)):
    sum+=(cards[i]*(n-i))

sum+=cards[0]*(n-1)

print(sum)
