#Compare BruteForce and Recurrence method for Maximum subarray Problem
##To Find the Maximum sum subarray of A
#s%
import math
from time import time
import numpy as np
import random
#A = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
A = [-3,-8,-9,-5,-6,-2]


def Max_crossing_subarray(A,low,high,mid):
    #print("Mid",mid)
    left_sum = -math.inf
    sum = 0
    Maxleft = 0
    for i in range(mid,low-1,-1):
        #print("Left",A[i])
        sum = sum + A[i]
        if sum > left_sum:
            left_sum = sum
            Maxleft = i

    right_sum = -math.inf
    sum = 0
    Maxright = 0
    for j in range(mid+1,high+1):
        #print("Right",A[j])
        sum = sum + A[j]
        if sum > right_sum:
            right_sum = sum
            Maxright = j

    return(left_sum+right_sum,Maxleft,Maxright)


def Max_sum_subarray(A,low,high):  #Func for finding Maximum subarray using Recurrence
    if low == high:
        return(A[low],low,high)
    else:
        mid = math.floor((low+high)/2)
        left_sum,left_low,left_high = Max_sum_subarray(A,low,mid)
        right_sum,right_low,right_high = Max_sum_subarray(A,mid+1,high)
        cross_sum,cross_low,cross_high = Max_crossing_subarray(A,low,high,mid)

        #print("Left sum : ",left_sum,"Right sum : ",right_sum,"Cross sum : ",cross_sum)

        if((left_sum >= right_sum)&(left_sum >= cross_sum)):
            return (left_sum,left_low,left_high)
        elif((right_sum >= left_sum)&(right_sum >= cross_sum)):
            return (right_sum,right_low,right_high)
        else:
            return (cross_sum,cross_low,cross_high)







def Brute_Force_Max_subarray(A):   # Func for finding MAximum subarray using Brute force
    length = len(A)

    Max_sum = -math.inf
    left = 0
    right = 0
    for i in range(len(A)):
        sum = A[i]
        for j in range(len(A)):

            if(i<j):
               #print(i,j)
               sum = sum + A[j]
        #print("sum is : ",sum)
            if (sum > Max_sum):
               left = i
               right = j
               Max_sum = sum
        #print("Maxsum is : ",Max_sum)
    return Max_sum


Running_time_Brute = []
Running_time_Recurrence = []

for i in range(5,100):
    A = [ random.randint(-100,100) for k in range(0,i)]
    random.shuffle(A)
    #print(A)
    #print(len(A))
    t0 = time()
    result1 = Brute_Force_Max_subarray(A)
    t1 = time()
    result2 = Max_sum_subarray(A,0,len(A)-1)
    t2 = time()
    Running_time_Brute.append(t1-t0)
    Running_time_Recurrence.append(t2-t1)
    print()


import matplotlib.pyplot as plt
#print(Running_time_Brute)
#print(Running_time_Recurrence)

plt.plot(Running_time_Brute,'b')
plt.plot(Running_time_Recurrence,'g')
plt.ylabel('Exectution time(in ms)')
plt.xlabel('size of input')

plt.show()


#print(Max_sum_subarray(A,0,len(A)-1))
