from sympy import*
import sympy as sp
A=sp.Matrix([[4,3],[6,3]])
L,U,_=A.LUdecomposition()
sp.pprint(L)
sp.pprint(U)