def solution(brown, yellow):
    answer = []
    xy=brown+yellow
    for i in range(1,xy):
        if xy%i!=0:
            continue
        elif xy%i==0:
            x=i
            y=xy//i
            if ((2*i+2*y-4)==brown) and ((xy-2*x-2*y+4)==yellow) and (x>=y):
                answer.append(x)
                answer.append(y)
                break
            else:
                continue
    return answer
