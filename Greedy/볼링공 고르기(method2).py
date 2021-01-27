n,m=map(int,input().split())
balls=list(map(int,input().split()))
# 조합의 방법을 사용하지 않고 하는 경우

def possibles(i,count):
    for k in range(i,n):
        for j in range(1,n-i):
            if (balls[i]!=balls[i+j]):
                count+=1
        i+=1
        possibles(i,count)
    return count

print(possibles(0,0))
            
    
