'''
This is a file explaining about 1, 2 and 3 dimensional array with for loop.
'''

# define array length for each dimension

arr1d_length = 5
arr2d_length = 3
arr3d_length = 4

# 1d array

arr1d = []                           # Create an empty list
for i in range(arr1d_length):        # Iterate through x_array_length
    arr1d.append(i)                  #     Append i into the list
print('\narr1d:\n{}'.format(arr1d))  # Print the list to check

# 2d array

arr2d = []                           # Create an empty list
for i in range(arr1d_length):        # Iterate through x_array_length
    arr1d_temp = []                  #     Create an temporary empty list for y_array_length
    for j in range(arr2d_length):    #     Iterate through y_array_length
        arr1d_temp.append(j)         #         Append j(y_array_length) into the temporary list
    arr2d.append(arr1d_temp)         #     Append the temporary list into the parent list
print('\narr2d:\n{}'.format(arr2d))  # Print the list to check

# 3d array

arr3d = []                             # create an empty list
for i in range(arr1d_length):          # iterate through x_array_length
    arr2d_temp = []                    # create a temporary empty list
    for j in range(arr2d_length):      # jiterate through y_array_length
        arr1d_tmep = []                # create a temporary empty list
        for k in range(arr3d_length):  # iterate through z_array_length
            arr1d_tmep.append(k)       # append k into the list
        arr2d_temp.append(arr1d_tmep)  # append the list into the parent list
    arr3d.append(arr2d_temp)           # append the list into the grand parent list
print('\narr3d\n{}'.format(arr3d))     # print the list to check

# equivallent

# arr1d with list comprehension

arr1d_comp = [i for i in range(arr1d_length)]
print('\narr1d and arr1d_comp are same: {}'.format(arr1d==arr1d_comp))

# arr2d with list comprehension

arr2d_comp = [[j for j in range(arr2d_length)] for i in range(arr1d_length)]
print('\narr2d and arr2d_comp are same: {}'.format(arr2d==arr2d_comp))

# arr3d with list comprehension

arr3d_comp = [[[k for k in range(arr3d_length)] for j in range(arr2d_length)] for i in range(arr1d_length)]
print('\narr3d and arr3d_comp are same: {}'.format(arr3d==arr3d_comp))
