from sympy import Matrix
A=Matrix([[12,-7,15],
        [-15,10,11]])
        
print("The Given Matrix is :\n")
print(A)
print("This is transpose:\n")
print(A.T)
print("The determinant is not defined because the matrix is not square.")
print("The Not exists")
print("The Reduced matrix in row echelon form:\n")
print(A.rref())
print("The rank is :\n")
print(A.rank())



