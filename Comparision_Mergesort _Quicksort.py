import math
from time import time
import numpy as np
import random




def Merge(A,p,q,r):
    M1 = [A[i] for i in range(p,q+1)]
    M2 = [A[i] for i in range(q+1,r+1)]

    length = len(M1) + len(M2)


    i = 0
    j = 0
    for k in range(p,r+1):
        if(M1[i] > M2[j]):
            A[k] = M2[j]
            j+=1
        else:
            A[k] = M1[i]
            i+=1

        if(i > len(M1)-1):

            while(j <= len(M2)-1):
                k+=1
                A[k] = M2[j]
                j+=1
            return
        if(j > len(M2)-1):

            while(i <= len(M1)-1):
                k+=1
                A[k] = M1[i]
                i+=1
            return






def Mergesort(A,p,r):
    q = math.floor((r+p)/2)
    if p < r:
        Mergesort(A,p,q)
        Mergesort(A,q+1,r)
        Merge(A,p,q,r)





def find_pivot(A,p,q):
    pivot  = A[p]
    i = p
    for j in range(i+1,q+1,1):
        if A[j] < pivot:

            temp = A[i+1]
            A[i+1] = A[j]
            A[j] = temp


            i = i + 1

    temp  = A[i]
    A[i] = pivot
    pivot = temp

    A[p] = pivot

    return i



def Quicksort(A,p,q):
    if p < q:
        r = find_pivot(A,p,q)
        Quicksort(A,p,r)
        Quicksort(A,r+1,q)


Running_time_Quicksort = []
Running_time_Mergesort = []

for i in range(5,1000):
    A = [ random.randint(-100,100) for k in range(0,i)]
    random.shuffle(A)
    print(A)
    print(len(A))
    t0 = time()
    A1 = A.copy()
    A2 = A.copy()
    result1 = Quicksort(A1,0,len(A)-1)
    t1 = time()
    result2 = Mergesort(A2,0,len(A)-1)
    t2 = time()
    Running_time_Quicksort.append(t1-t0)
    Running_time_Mergesort.append(t2-t1)
    print()


import matplotlib.pyplot as plt


plt.plot(Running_time_Quicksort,'b')
plt.plot(Running_time_Mergesort,'g')
plt.ylabel('Exectution time(in ms)')
plt.xlabel('size of input')

plt.show()
