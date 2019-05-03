import random
from time import time
import math
from numpy import *
import numpy

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

    #print()
    #print("A11",A11)
    #print()
    #print("A12",A12.tolist())
    #print()
    #print("A21",A21.tolist())
    #print()
    #print("A22",A22.tolist())
    #print()
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

    K1  = A11 + A22


    K2 = numpy.zeros(shape=(l,l),dtype=int).tolist()

    K2 = B11 + B22



    K3 = numpy.zeros(shape=(l,l),dtype=int).tolist()

    K3 = A21 + A22




    K4= numpy.zeros(shape=(l,l),dtype=int).tolist()



    K4 = B12 - B22





    K5 = numpy.zeros(shape=(l,l),dtype=int).tolist()

    K5 = B21 - B11




    K6 = numpy.zeros(shape=(l,l),dtype=int).tolist()

    K6 = A11 + A12






    K7 = numpy.zeros(shape=(l,l),dtype=int).tolist()

    K7 = A21 - A11


    K8 = numpy.zeros(shape=(l,l),dtype=int).tolist()

    K8 = B11 + B12





    K9 = numpy.zeros(shape=(l,l),dtype=int).tolist()

    K9 = A12 - A22



    K10 = numpy.zeros(shape=(l,l),dtype=int).tolist()

    K10 = B21 + B22










    P1 =  numpy.zeros(shape=(l,l),dtype=int)


    P1 = numpy.array(strassen_matrix_multiplication(K1,K2))



    P2 =  numpy.zeros(shape=(l,l),dtype=int)



    P2 = numpy.array(strassen_matrix_multiplication(K3,B11))




    P3 =  numpy.zeros(shape=(l,l),dtype=int)

    P3 = numpy.array(strassen_matrix_multiplication(A11,K4))




    P4 =  numpy.zeros(shape=(l,l),dtype=int)

    P4 = numpy.array(strassen_matrix_multiplication(A22,K5))





    P5 =  numpy.zeros(shape=(l,l),dtype=int)

    P5 = numpy.array(strassen_matrix_multiplication(K6,B22))



    P6 =  numpy.zeros(shape=(l,l),dtype=int)

    P6 = numpy.array(strassen_matrix_multiplication(K7,K8))



    P7 =  numpy.zeros(shape=(l,l),dtype=int)

    P7 = numpy.array(strassen_matrix_multiplication(K9,K10))



#C11=M1+M4−M5+M7
#C12=M3+M5
#C21=M2+M4
#C22=M1−M2+M3 +M6
    L1 =  numpy.zeros(shape=(l,l),dtype=int)

    L1 = P1 + P4

    L2 =  numpy.zeros(shape=(l,l),dtype=int)

    L2 = P7 + numpy.negative(P5)

    C11 =  numpy.zeros(shape=(l,l),dtype=int)

    C11 = L1 + L2


    C12 = numpy.zeros(shape=(l,l),dtype=int)

    C12 = P3 + P5

    C21 = numpy.zeros(shape=(l,l),dtype=int)

    C21 = P2 + P4


    L3 = numpy.zeros(shape=(l,l),dtype=int)

    L3 = P1 + numpy.negative(P2)

    L4 = numpy.zeros(shape=(l,l),dtype=int)

    L4 = P3 + P6


    C22 = numpy.zeros(shape=(l,l),dtype=int)

    C22 = L3 + L4


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
    C11 = C11.tolist()
    C12 = C12.tolist()
    C21 = C21.tolist()
    C22 = C22.tolist()
    #print(type(C12))
    C1 = numpy.zeros(shape=(l,l),dtype=int).tolist()
    C2 = numpy.zeros(shape=(l,l),dtype=int).tolist()
    C = []

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

    return C


def Brute_Force_Matrix_Multi(A,B):
       n = len(A)

       c = []

       for i in range(n):
           c.append([0]*n)



       for i in range(n):
           for j in range(n):
               c[i][j] = 0
               for k in range(n):
                   c[i][j] = A[i][k]*B[k][j] + c[i][j]
       return c








Running_time_Brute = []
Running_time_Recurrence = []
i = 2
while i < 65:
    A = [ [random.randint(-100,100) for k in range(0,i)]for t in range(0,i)]
    B = [ [random.randint(-100,100) for k in range(0,i)]for t in range(0,i)]
    random.shuffle(A)
    print(A)
    print()
    print()
    print(B)
    print(len(A),len(B))
    t0 = time()
    result1 = Brute_Force_Matrix_Multi(A,B)

    t1 = time()
    result2 = strassen_matrix_multiplication(A,B)
    t2 = time()
    Running_time_Brute.append(t1-t0)
    Running_time_Recurrence.append(t2-t1)
    print()
    print()
    i *= 2



import matplotlib.pyplot as plt
#print(Running_time_Brute)
#print(Running_time_Recurrence)

plt.plot(Running_time_Brute,'b')
plt.plot(Running_time_Recurrence,'g')
plt.ylabel('Exectution time(in ms)')
plt.xlabel('size of input')

plt.show()
