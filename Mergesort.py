import math

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






A = [6,10,13,5,8,3,2,11]
print(A)
Mergesort(A,0,7)
print(A)
