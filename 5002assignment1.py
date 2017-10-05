import numpy as np
# Adding a dataset as in Table 1.
Attributes1 = [-1, -2, -3, 1, 2, 3, 1]
Attributes2 = [-1, -1, -2, 1, 1, 2, 2]
Attributes3 = [1, 4, -2, 1, 2, 1, 4]
# packed array
data_set = np.vstack([Attributes1, Attributes2, Attributes3])
print([Attributes1, Attributes2, Attributes3])
# computing covariance matrix
covariance_matrix = np.cov(data_set)
print(covariance_matrix)
# computing eigenvalues and eigenvectors
from numpy import linalg as LA
eigenvalues, eigenvectors = LA.eig(covariance_matrix)
print(eigenvectors, eigenvalues)
# computing the proportion
eigenvalues.sort()
proportion = sum(eigenvalues[-2:]) / sum(eigenvalues)
print (proportion)