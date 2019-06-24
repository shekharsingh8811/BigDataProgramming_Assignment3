## Excercise 1 : Replace all odd numbers in arr with -1 ##
import numpy as np
arr=np.array([0,1,2,3,4,5,6,7,8,9])
modified_arr=np.where(arr%2==1, -1, arr) 
print(modified_arr)


## Excercise 2 : Convert a 1D array to a 2D array with 2 rows ##
import numpy as np
arr=np.arange(10)
modified_arr = np.reshape(arr, (2, 5))
print(modified_arr)


## Excercise 3 : Create a patern with hardcoding ##
import numpy as np
arr=np.array([1,2,3])
seq=np.repeat(arr,3)
tile=np.tile(arr,3)
modified_arr=np.r_[seq,tile]
print(modified_arr)


## Excercise 4 : Get the commom items between a and b ##
import numpy as np
a=np.array([1,2,3,2,3,4,3,4,5,6])
b=np.array([7,2,10,2,7,4,9,4,9,8])
common_arr = np.intersect1d(a, b)
print(common_arr)


## Excercise 5 : Get the positions where elements of a and b match ##
import numpy as np
a=np.array([1,2,3,2,3,4,3,4,5,6])
b=np.array([7,2,10,2,7,4,9,4,9,8])
indices_arr = np.where(np.in1d(a, b))[0]
print(indices_arr)


## Excercise 6 : Create a 2D array of shape 5*3 to contain random decimal number between 5 and 10 ##
import numpy as np
arr=np.random.uniform(5,10, size=(5, 3))
print(arr)


## Excercise 7 : Limit the number of items printed in python numpy array to a maximum of 6 elements ##
import numpy as np
np.set_printoptions(threshold=3, edgeitems=3)
arr=np.arange(15)
print(arr)


## Excercise 8 : Pretty print a numpy array by supressing the scientific notation ##
import numpy as np
np.set_printoptions(precision=6, suppress=True)
np.random.seed(100)
rand_arr=np.random.random([3,3])/1e3
print(rand_arr)


## Excercise 9 : Swap two columns in a 2D numpy array ##
import numpy as np
arr=np.arange(9).reshape(3,3)
arr[:,[0, 2]] = arr[:,[2, 0]]
print(arr)


## Excercise 10 : Swap two rows in a 2D numpy array ##
import numpy as np
arr=np.arange(9).reshape(3,3)
arr[[0, 1],:] = arr[[1, 0],:]
print(arr)