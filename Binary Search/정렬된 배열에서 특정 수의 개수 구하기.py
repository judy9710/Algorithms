n,x=map(int,input().split())
import sys
input=sys.stdin.readline
array=list(map(int,input().split()))

from bisect import bisect_left, bisect_right

def counting(array,left_value,right_value):
    left=bisect_left(array,left_value)
    right=bisect_right(array,right_value)
    result=right-left
    if result==0:
        return -1
    else:
        return result

print(counting(array,x,x))
