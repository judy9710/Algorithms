n,k=map(int,input().split())

result=n
count=0

while result!=1:
    if result%k ==0:
        result = result//k
        count+=1
    else:
        result-=1
        count+=1
        
print(count)
