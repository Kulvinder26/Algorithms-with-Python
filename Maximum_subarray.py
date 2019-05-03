##To Find the Maximum sum subarray of A
#s%
import math
from math import floor
#A = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
A = [-3,-8,-9,-5,-6,-2]


def Max_crossing_subarray(A,low,high,mid):
    for i in range(low,high+1):
        print("Elementary ",A[i])
    print("Mid",mid)
    left_sum = -math.inf
    sum = 0
    Maxleft = 0
    for i in range(mid,low-1,-1):
        print("Left",A[i])
        sum = sum + A[i]
        if sum > left_sum:
            left_sum = sum
            Maxleft = i

    right_sum = -math.inf
    sum = 0
    Maxright = 0
    for j in range(mid+1,high+1):
        print("Right",A[j])
        sum = sum + A[j]
        if sum > right_sum:
            right_sum = sum
            Maxright = j

    return(left_sum+right_sum,Maxleft,Maxright)


def Max_sum_subarray(A,low,high):
    if low == high:
        return(A[low],low,high)
    else:
        mid = floor((low+high)/2)
        left_sum,left_low,left_high = Max_sum_subarray(A,low,mid)
        right_sum,right_low,right_high = Max_sum_subarray(A,mid+1,high)
        cross_sum,cross_low,cross_high = Max_crossing_subarray(A,low,high,mid)

        print("Left sum : ",left_sum,"Right sum : ",right_sum,"Cross sum : ",cross_sum)

        if((left_sum >= right_sum)&(left_sum >= cross_sum)):
            return (left_sum,left_low,left_high)
        elif((right_sum >= left_sum)&(right_sum >= cross_sum)):
            return (right_sum,right_low,right_high)
        else:
            return (cross_sum,cross_low,cross_high)





print(Max_sum_subarray(A,0,len(A)-1))
