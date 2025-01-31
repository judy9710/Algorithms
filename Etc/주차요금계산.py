import math

def cal(hour):
    return 60*int(hour[:2])+int(hour[3:])

def solution(fees, records):
    answer = []
    in_q=dict()
    acc=dict()
    unique=set()
    for r in records:
        s,n,b=r.split(' ')
        unique.add(n)
    unique_n=len(unique)
    for u in unique:
        acc[u]=0
    for record in records:
        s,n,b=record.split(' ')
        if b=='IN':
            in_q[n]=s
        elif b=='OUT':
            start,number=in_q[n],n
            del in_q[n]
            lasting=cal(s)-cal(start)
            acc[number]+=lasting
            #print(acc)
    
    remain=len(in_q)
    
    while remain!=0:
        for k, v in zip(in_q.keys(), in_q.values()):
            start=v
            number=k
            remain-=1
            lasting=cal('23:59')-cal(start)
            acc[number]+=lasting
    #print(acc)
    acc_=list(acc)
    #print(acc)
    acc_.sort()
    #print(acc)
    for a in acc_:
        if acc[a]<fees[0]:
            answer.append(fees[1])
            continue
        if (acc[a]-fees[0])%fees[2]!=0:
            result=(acc[a]-fees[0])//fees[2]
            result+=1
        else:
            result=(acc[a]-fees[0])//fees[2]
        #print(math.ceil((acc[a]-fees[0])//fees[2]))
        answer.append(fees[1]+result*fees[3])
    
    return answer
