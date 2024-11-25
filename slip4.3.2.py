from sympy import*
import sympy as sp
A=sp.Matrix([[10,2,3],[12,7,15],[-12,10,-11]])
sp.pprint(A.T)
print(A.nullspace())
sp.pprint(A.inv())
sp.pprint(A.rref())
print(A.rank())