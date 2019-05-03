#a = [[1,3,5],
#     [2,5,1],
#     [1,1,3]]

#b = [[2,1,4],
#     [1,5,5],
#     [3,2,1]]


a = [[3,5,7,8],
     [1,2,8,7],
     [4,5,3,-2],
     [1,6,7,9]]

b = [[2,8,6,9],
     [3,-5,6,7],
     [1,4,9,-3],
     [10,-2,5,2]]

def Brute_Force_Matrix_Multi(A,B):
       n = len(a)

       c = []

       for i in range(n):
           c.append([0]*n)



       for i in range(n):
           for j in range(n):
               c[i][j] = 0
               for k in range(n):
                   c[i][j] = a[i][k]*b[k][j] + c[i][j]
       return c



Matrix = Brute_Force_Matrix_Multi(a,b)
print(Matrix)
