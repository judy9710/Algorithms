n,m=map(int,input().split())
rice_cake=list(map(int,input().split()))
maximum_length=max(rice_cake)

def maximum_height():
    for h in range(maximum_length):
        sum=0
        for j in rice_cake:
            if j<=h:
                sum+=0
            else:
                sum+=(j-h)
        if sum>m:
            continue
        elif sum<m:
            return h-1
        else:
            return h
        
print(maximum_height())
