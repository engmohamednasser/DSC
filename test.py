
import numpy as np 

print("hello python docker")


x=7
result=np.sqrt(x)
print("result=" ,result)


arr = np.array([(1,2,3),(4,5,6)])
print(arr.ndim)




a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])


row_r1 = a[1, :]    
row_r2 = a[1:2, :] 
print(row_r1, row_r1.shape)  
print(row_r2, row_r2.shape)  


col_r1 = a[:, 1]
col_r2 = a[:, 1:2]
print(col_r1, col_r1.shape)  
print(col_r2, col_r2.shape) 




x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)


print(x + y)
print(np.add(x, y))

print(x - y)
print(np.subtract(x, y))

print(x * y)
print(np.multiply(x, y))


print(x / y)
print(np.divide(x, y))

print(np.sqrt(x))
