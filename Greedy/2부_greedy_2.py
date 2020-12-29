n,m,k=map(int, input().split())
arr=list(map(int, input().split()))

arr.sort()

maximum=arr[n-1]
next_maximum=arr[n-2]

if maximum==next_maximum:
    for i in range(3,n):
        next_maximum=arr[n-i]
        if maximum!=next_maximum:
            break

count=m//k
next_count=m%k

print(count*maximum*k+next_count*next_maximum)
