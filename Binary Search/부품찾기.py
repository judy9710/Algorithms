# 이진탐색으로 하면 가장 시간 복잡도가 적게 걸릴 것으로 예상된다.

results=[]
def search_items(array,target,start,end):
    if start>end:
        return None
    mid=(start+end)//2
    if array[mid]==target:
        return mid
    elif array[mid]>target:
        return search_items(array,target,start,mid-1)
    else:
        return search_items(array,target,mid+1,end)

n=int(input())
items=list(map(int,input().split()))

#이진 탐색은 정렬이 되어있다는 것이 기본 전제이므로 정렬을 수행한다.
items.sort()
print(items)
m=int(input())
wanted_items=list(map(int,input().split()))

for i in wanted_items:
    result=search_items(items,i,0,n-1)
    if result==None:
        results.append('no')
    else:
        results.append('yes')
        
for j in results:
    print(j,end=' ')
