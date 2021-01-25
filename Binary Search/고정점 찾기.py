n=int(input())
data=list(map(int,input().split()))

def find_fixed_point(array,start,end):
    while start<=end:
        mid=(start+end)//2
        if array[mid]==mid:
            return mid
        elif array[mid]>mid:
            end=mid-1
        else:
            start=mid+1
    return None

result=find_fixed_point(data,0,n-1)

if result==None:
    print(-1)
else:
    print(result)
