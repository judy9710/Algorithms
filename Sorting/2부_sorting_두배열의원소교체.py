n,k=map(int,input().split())

a=list(map(int,input().split()))
b=list(map(int,input().split()))

new_a=sorted(a)
new_b=sorted(b,reverse=True)

for i in range(k): #정렬이 되어있으므로 k번 반복하는 것이 최대합을 구하는 것을 보장해준다.
    if new_a[i]<new_b[i]:
        new_a[i]=new_b[i] #문제는 a의 합만 구하는 것이므로 a에만 값을 업데이트 해주면 된다.

print(sum(new_a))




