from sympy import*
import sympy as sp
A=sp.Matrix([[1,2,4],[0,1,5],[-2,-4,3]])
minors=sp.Matrix.zeros(A.rows,A.cols)
cofactors=sp.Matrix.zeros(A.rows,A.cols)
for i in range(A.rows):
    for j in range(A.cols):
        minor=A.minor(i,j)
        minors[i,j]=minor
        cofactor=(-1)**(i+j)*minor
        cofactors[i,j]=cofactor

print("this is orignal matrix:\n")
sp.pprint(A)
print("This is Minor :\n")
sp.pprint(minors)
print("this is cofactor:\n")
sp.pprint(cofactors)