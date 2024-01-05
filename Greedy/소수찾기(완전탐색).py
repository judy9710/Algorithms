from itertools import permutations

def solution(numbers):
    answer = 0
    # 소수의 판별을 위한 코드가 필요함
    # 모든 길이의 경우의 수를 따지가 위한 장치가 필요할 것임
    # 우선 문자열을 전부 하나씩 split하자
    results=[]
    unique=[]
    for c in numbers:
        results.append(int(c))
    #print(results)
    for i in range(1,len(results)+1):
        result=list(permutations(results,i))
        #print(result)
        
        for i in result:
            if len(i)==1:
                #prime인지 체크하고
                r=i[0]
                #print(r)
            elif len(i)==2:
                r=10*i[0]+i[1]
                #print(10*i[0]+i[1])
            elif len(i)==3:
                r=100*i[0]+10*i[1]+i[2]
                #print(100*i[0]+10*i[1]+i[2])
            elif len(i)==4:
                r=1000*i[0]+100*i[1]+10*i[2]+i[3]
                #print(1000*i[0]+100*i[1]+10*i[2]+i[3])
            elif len(i)==5:
                r=10000*i[0]+1000*i[1]+100*i[2]+10*i[3]+i[4]
                #print(10000*i[0]+1000*i[1]+100*i[2]+10*i[3]+i[4])
            elif len(i)==6:
                r=100000*i[0]+10000*i[1]+1000*i[2]+100*i[3]+10*i[4]+i[5]
                #print(100000*i[0]+10000*i[1]+1000*i[2]+100*i[3]+10*i[4]+i[5])
            elif len(i)==7:
                r=1000000*i[0]+100000*i[1]+10000*i[2]+1000*i[3]+100*i[4]+10*i[5]+i[6]
                #print(1000000*i[0]+100000*i[1]+10000*i[2]+1000*i[3]+100*i[4]+10*i[5]+i[6])
            #print(r)
            unique.append(r)
    uniques=set(unique)
    #print(uniques)
    for u in uniques:
        if isPrime(u):
            answer+=1
    return answer

def isPrime(n):
    if n==1 or n==0:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
