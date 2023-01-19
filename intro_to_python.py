import numpy as np
###list = test_intro_to_python.py###
list = 0
if list == 0 :
  list = ([1,2,3], [4,5,6], [7,8,9])
matrix = np.asmatrix(list)
for r in range(3):
  for c in range(3):
    if r == c :
      matrix[r,c] = 1
    if r != c :
      matrix[r,c] = 0
print(matrix)
for r in range(3):
  for c in range(3):
    if r != c :
      matrix[r,c] += 3
print(matrix)
matrix = matrix[:,0:2]
print(matrix)