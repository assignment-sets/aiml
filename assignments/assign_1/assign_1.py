import numpy as np

# 1
arr = np.array([0, 1, 2])
print(arr)

#2
arr = np.arange(0, 3, 1)
print(arr)

# 3
arr = np.zeros(3, dtype=int)
print(arr)

# 4
mat = np.array( [[0, 1], [2, 3]])
print(mat)

#5
mat = np.arange(4).reshape(2, 2)
print(mat)

#6
mat = np.arange(4).reshape(2, 2)
print(mat.shape)

#7
arr = np.array([0, 1, 2])
avg = np.average(arr)
print(avg)

#8
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
res = v1 + v2
print(res)

#9
arr = np.array([0, 1, 2])
print(np.sum(arr))

#10
arr = np.array([0, 1, 2])
print(np.sqrt(arr))

#11
my_list = [1, 2, 3]
vec = np.array(my_list)
print(vec)

#12
arr = np.arange(4, 13, 1).reshape(3, 3)
print(arr)

#13
v = np.zeros(10, dtype=int)
v[5] = 15
print(v)

#14
arr = np.array([0, 1, 2])
print(np.flip(arr))

#15
def create_border_array(rows, cols):
    array = np.zeros((rows, cols), dtype=int)
    
    array[0, :] = 1         # Top border
    array[-1, :] = 1        # Bottom border
    array[:, 0] = 1         # Left border
    array[:, -1] = 1        # Right border
    
    print(array)
    
create_border_array(3, 3)

#16
def create_checkerboard(size):
    checkerboard = np.indices((size, size)).sum(axis=0) % 2
    return checkerboard

checkerboard_matrix = create_checkerboard(8)
print(checkerboard_matrix)

#17
arr = np.arange(4, 13, 1).reshape(3, 3)
np.savetxt(r'C:\file.txt', arr, fmt='%d')