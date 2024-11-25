from sympy import*
import sympy as sp
U=sp.Matrix([2,5,-3])
V=sp.Matrix([1,0,-2])
sp.pprint(U+V)
sp.pprint(4*U)
sp.pprint(U-V)
sp.pprint((2*U)+(3*V))
sp.pprint(eye(3))
