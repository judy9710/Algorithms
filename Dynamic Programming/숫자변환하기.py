def solution(x,y,n):
    INF=1e9
    d=[INF]*(y+1)
    d[x]=0
    if x==y:
        return 0
    for i in range(x,y+1):
        if d[i]==INF:
            continue
        if (i+n)<=y:
            d[i+n]=min(d[i+n], d[i]+1)
        if (i*2)<=y:
            d[i*2]=min(d[i*2], d[i]+1)
        if (i*3)<=y:
            d[i*3]=min(d[i*3], d[i]+1)
    if d[y]==INF:
        return -1
    return d[y]
