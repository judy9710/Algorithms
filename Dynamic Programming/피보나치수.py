import sys
sys.setrecursionlimit(10**7)

def solution(n):
    answer = 0
    answer=fibonacci(n)%1234567
    return answer

def fibonacci(n):
    fib=[0]*100001
    fib[0]=0
    fib[1]=1
    for i in range(2,n+1):
        fib[i]=fib[i-1]+fib[i-2]
    answer=fib[n]
    return answer
    
