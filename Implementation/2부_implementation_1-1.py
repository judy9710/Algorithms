n=int(input())
direction=list(map(str, input().split()))
current=[1,1]

while direction!=[]:
    if direction[0]=='L':
        current=[sum(x) for x in zip(current,[0,-1])]
        del direction[0]
        if (current[0]<1 or current[0]>n) or (current[1]<1 or current[1]>n):
            current=[sum(x) for x in zip(current, [0,1])]
    elif direction[0]=='R':
        current=[sum(x) for x in zip(current,[0,1])]
        del direction[0]
        if (current[0]<1 or current[0]>n) or (current[1]<1 or current[1]>n):
            current=[sum(x) for x in zip(current, [0,-1])]
    elif direction[0]=='U':
        current=[sum(x) for x in zip(current,[-1,0])]
        del direction[0]
        if (current[0]<1 or current[0]>n) or (current[1]<1 or current[1]>n):
            current=[sum(x) for x in zip(current, [1,0])]
    elif direction[0]=='D':
        current=[sum(x) for x in zip(current,[1,0])]
        del direction[0]
        if (current[0]<1 or current[0]>n) or (current[1]<1 or current[1]>n):
            current=[sum(x) for x in zip(current, [-1,0])]
print(current)
