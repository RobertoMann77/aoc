#https://problemsolvingwithpython.com/05-NumPy-and-Arrays/05.08-Systems-of-Linear-Equations/

import numpy as np

A = np.array([[8, 3, -2], [-4, 7, 5], [3, 4, -12]])
b = np.array([9, 15, 35])
x = np.linalg.solve(A, b)
x