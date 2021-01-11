n=int(input())
item_list=set(map(int,input().split()))

m=int(input())
wanted_list=list(map(int,input().split()))

for i in wanted_list:
    if i in item_list:
        print('yes',end=' ')
    else:
        print('no',end=' ')
