g=int(input())
p=int(input())
boarding_place=[]
for _ in range(p):
    boarding_place.append(int(input()))

dp=[i for i in range(p+1)]

count=0


for i in boarding_place:
    if dp[i]!=0:
        dp[i]=dp[i]-1
        count+=1
    if (sum(dp[j])==0 for j in range(i+1)):
        break
    if dp[i]==0:
        for j in range(i+1):
            dp[j]=0
    if (sum(dp[j])==0 for j in range(i+1)):
        dp[i+1]=1

print(count)

    
