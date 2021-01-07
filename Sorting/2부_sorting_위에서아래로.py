n=int(input())

array=[int(input()) for _ in range(n)]

new_array=sorted(array, reverse=True)

for i in new_array:
    print(i,end=' ')
