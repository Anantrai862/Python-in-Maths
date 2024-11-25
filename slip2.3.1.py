from sympy import*
import sympy as sp
A=sp.Matrix([[16,10,11],[18,-7,7],[-1,9,-13]])
sp.pprint(A.T)
print(A.det(),'\n')
sp.pprint(A.inv())
sp.pprint(A.rref())
sp.pprint(A.row_insert(1,Matrix([[0,5,4]])))