from sympy import*
import sympy as sp
A=sp.Matrix([[1,2,3],[0,1,4],[5,6,0]])
minors = sp.Matrix.zeros(A.rows,A.cols)
cofactors= sp.Matrix.zeros(A.rows,A.cols)
for i in range(A.rows):
    for j in range(A.cols):
        minor=A.minor(i,j)
        minors[i,j]=minor
        cofactor=(-1)**(i+j)*minor
        cofactors[i,j]=cofactor
print("\nOrignal matrix:")
sp.pprint(A)
print("\nMatrix of Minor")
sp.pprint(minors)
print("\nMatrix of cofactor:")
sp.pprint(cofactors)