'''
This is a file explaining about a difference between index and item
'''

# import compas module
from compas.geometry import Point
from compas_view2.app import App

# define array length for each dimension
arr1d_length = 2
arr2d_length = 2
arr3d_length = 2

# 1d array with item
arr1d = [Point(i, 0, 0) for i in range(arr1d_length)]
print('\narr1d: {}'.format(arr1d))

# break down the 1d array...
for index, item in enumerate(arr1d):
    print('\nindex: {}, \nitem: {}'.format(index, item))

# 2d array with item
arr2d = [[Point(i, j, 0) for j in range(arr2d_length)] for i in range(arr1d_length)]
print('\narr2d: {}'.format(arr2d))

# break down the 2d array...
for index_i, arr1d_temp in enumerate(arr2d):
    for index_j, item in enumerate(arr1d_temp):
        print('\nindex_i: {}, \nindex_j: {}, \nitem: {}'.format(index_i, index_j, item))

# 3d array with item
arr3d = [[[Point(i, j, k) for k in range(arr3d_length)] for j in range(arr2d_length)] for i in range(arr1d_length)]
print('\narr3d: {}'.format(arr3d))

# break doewn the 3d array
for index_i, arr2d_temp in enumerate(arr3d):
    for index_j, arr1d_temp in enumerate(arr2d_temp):
        for index_k, item in enumerate(arr1d_temp):
            print('\nindex_i: {}, \nindex_j: {}, \nindex_k: {}, \nitem: {}'.format(index_i, index_j, index_k, item))


# visualize with compas view2
viewer = App()
arr1d = [viewer.add(i) for i in arr1d]
arr2d = [[viewer.add(j) for j in i] for i in arr2d]
arr3d = [[[viewer.add(k) for k in j] for j in i] for i in arr3d]
viewer.run()
