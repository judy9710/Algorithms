x,y=map(str, input().split())
possible=[x for x in range(1,9)]
y=int(y)

if x=='a':
    x=1
elif x=='b':
    x=2
elif x=='c':
    x=3
elif x=='d':
    x=4
elif x=='e':
    x=5
elif x=='f':
    x=6
elif x=='g':
    x=7
elif x=='h':
    x=8

count=0

next_jump=[[x-2,y-1],[x-2,y+1],[x+2,y-1],[x+2,y+1],[x-1,y-2],[x-1,y+2],[x+1,y-2],[x+1,y+2]]

for i in next_jump:
    if i[0] in possible and i[1] in possible:
        count+=1
print(count)
