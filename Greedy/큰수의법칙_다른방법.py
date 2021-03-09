n,m,k=map(int,input().split())
data=list(map(int,input().split()))


data.sort()
first=data[n-1]
second=data[n-2]

result=0
count=0

while True:
  if m<k:
    result=first*m
    break
  if count==m:
    break
  result+=(first*k)
  count+=k
  if count>m:
    result-=first*(count-m)
    break
  result+=second
  count+=1

print(result)
