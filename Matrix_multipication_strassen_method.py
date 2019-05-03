import math
from numpy import *
import numpy

a = [[3,5,7,8],
     [1,2,8,7],
     [4,5,3,-2],
     [1,6,7,9]]

b = [[2,8,6,9],
     [3,-5,6,7],
     [1,4,9,-3],
     [10,-2,5,2]]

#a = [[1,3],
#     [7,5]]


#b = [[6,8],
#     [4,2]]



def strassen_matrix_multiplication(A,B):
    n = len(A)

    if n == 1:
        return [[A[0][0]*B[0][0]]]


    l = math.floor(n/2)

    Ak = array(A)
    Bk = array(B)
    #for i in range(l):

    A11 = Ak[0:l,0:l]
    A12 = Ak[0:l,l:n]
    A21 = Ak[l:n,0:l]
    A22 = Ak[l:n,l:n]

    B11 = Bk[0:l,0:l]
    B12 = Bk[0:l,l:n]
    B21 = Bk[l:n,0:l]
    B22 = Bk[l:n,l:n]

    print()
    print("A11",A11.tolist())
    print()
    print("A12",A12.tolist())
    print()
    print("A21",A21.tolist())
    print()
    print("A22",A22.tolist())
    print()
    K1 = []
    K2 = []
    K3 = []
    K4 = []
    K5 = []
    K6 = []
    K7 = []
    K8 = []
    K9 = []
    K10 = []

#M1= (A11+A22) (B11+B22)
#M2= (A21+A22)B11
#M3=A11(B12−B22)
#M4=A22(B21−B11)
#M5= (A11+A12)B22
#M6= (A21−A11)(B11+B12)
#M7= (A12−A22)(B21+B22)



    K1 = numpy.zeros(shape=(l,l),dtype=int).tolist()
    #print("K1",K1)
    for i in range(l):
        for j in range(l):

            K1[i][j] = A11[i][j] + A22[i][j]


    K2 = numpy.zeros(shape=(l,l),dtype=int).tolist()
    for i in range(l):
        for j in range(l):
            K2[i][j] = B11[i][j] + B22[i][j]



    K3 = numpy.zeros(shape=(l,l),dtype=int).tolist()

    for i in range(l):
        for j in range(l):

            K3[i][j] = A21[i][j] + A22[i][j]




    K4= numpy.zeros(shape=(l,l),dtype=int).tolist()

    for i in range(l):
        for j in range(l):

            K4[i][j] = B12[i][j] - B22[i][j]





    K5 = numpy.zeros(shape=(l,l),dtype=int).tolist()

    for i in range(l):
        for j in range(l):

            K5[i][j] = B21[i][j] - B11[i][j]




    K6 = numpy.zeros(shape=(l,l),dtype=int).tolist()

    for i in range(l):
        for j in range(l):

            K6[i][j] = A11[i][j] + A12[i][j]






    K7 = numpy.zeros(shape=(l,l),dtype=int).tolist()

    for i in range(l):
        for j in range(l):

            K7[i][j] = A21[i][j] - A11[i][j]


    K8 = numpy.zeros(shape=(l,l),dtype=int).tolist()

    for i in range(l):
        for j in range(l):

            K8[i][j] = B11[i][j] + B12[i][j]





    K9 = numpy.zeros(shape=(l,l),dtype=int).tolist()

    for i in range(l):
        for j in range(l):

            K9[i][j] = A12[i][j] - A22[i][j]



    K10 = numpy.zeros(shape=(l,l),dtype=int).tolist()

    for i in range(l):
        for j in range(l):

            K10[i][j] = B21[i][j] + B22[i][j]










    P1 = []

    for i in range(l):
        P1.append([0]*l)
    P1 = strassen_matrix_multiplication(K1,K2)



    P2 = []

    for i in range(l):
        P2.append([0]*l)

    P2 = strassen_matrix_multiplication(K3,B11)




    P3 = []

    for i in range(l):
        P3.append([0]*l)

    P3 = strassen_matrix_multiplication(A11,K4)




    P4 = []

    for i in range(l):
        P4.append([0]*l)

    P4 = strassen_matrix_multiplication(A22,K5)





    P5 = []

    for i in range(l):
        P5.append([0]*l)

    P5 = strassen_matrix_multiplication(K6,B22)



    P6 = []

    for i in range(l):
        P6.append([0]*l)

    P6 = strassen_matrix_multiplication(K7,K8)



    P7 = []

    for i in range(l):
        P7.append([0]*l)

    P7 = strassen_matrix_multiplication(K9,K10)



#C11=M1+M4−M5+M7
#C12=M3+M5
#C21=M2+M4
#C22=M1−M2+M3 +M6
    L1 = []

    for i in range(l):
        L1.append([0]*l)

    for i in range(l):
        for j in range(l):

            L1[i][j] = P1[i][j] + P4[i][j]

    L2 = []

    for i in range(l):
        L2.append([0]*l)

    for i in range(l):
        for j in range(l):

            L2[i][j] = -P5[i][j] + P7[i][j]

    C11 = []

    for i in range(l):
        C11.append([0]*l)

    for i in range(l):
        for j in range(l):

            C11[i][j] = L1[i][j] + L2[i][j]


    C12 = []

    for i in range(l):
        C12.append([0]*l)

    for i in range(l):
        for j in range(l):

            C12[i][j] = P3[i][j] + P5[i][j]

    C21 = []

    for i in range(l):
        C21.append([0]*l)

    for i in range(l):
        for j in range(l):

            C21[i][j] = P2[i][j] + P4[i][j]


    L3 = []

    for i in range(l):
        L3.append([0]*l)

    for i in range(l):
        for j in range(l):

            L3[i][j] = P1[i][j] - P2[i][j]

    L4 = []

    for i in range(l):
        L4.append([0]*l)

    for i in range(l):
        for j in range(l):

            L4[i][j] = P3[i][j] + P6[i][j]


    C22 = []

    for i in range(l):
        C22.append([0]*l)

    for i in range(l):
        for j in range(l):

            C22[i][j] = L3[i][j] + L4[i][j]


    print()
    print()
    print()
    #print("C11",C11)
    #print()
    #print("C12",C12)
    #print()
    #print("C21",C21)
    #print()
    #print("C22",C22)
    print(len(C11))
    C1 = []
    C2 = []
    C = []

    for i in range(l):
        C1.append([0]*l)


    for i in range(l):
        C2.append([0]*l)

    for i in range(l):
        C1[i] = C11[i][:] + C12[i][:]
        C2[i] = C21[i][:] + C22[i][:]


    for i in range(l):
        C.append([0]*l)
    #for i in range(l):
    C = C1 + C2

    #print("C1",C1)
    #print("C2",C2)
    #print()

    return C;






print("A:",a)
print()
print("B:",b)
Matrix = strassen_matrix_multiplication(a,b)
print(Matrix)
