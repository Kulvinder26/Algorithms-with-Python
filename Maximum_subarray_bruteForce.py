#Find the Maximum sum subarray of A using Brute Force method.
import math
A = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
#A = [-2,5,-3,1,2,6,-9,4,3]
def Brute_Force_Max_subarray(A):
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

print("Maximum sum",Brute_Force_Max_subarray(A))
