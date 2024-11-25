from sympy import*
import sympy as p

A=p.Matrix([[1,2,3],[0,1,4],[5,6,0]])
minors = p.Matrix.zeros(A.rows,A.cols)
for i in range(A.rows):
    for j in range(A.cols):
        fuck=A.minor(i,j)
        minors[i,j]=fuck
print(minors)