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




A = [6,10,13,5,8,3,2,11]
print(A)
Quicksort(A,0,7)
print(A)
