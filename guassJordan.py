import numpy as np

def guassJordan(A,b):
    mtx = np.concatenate((A, b), axis=1)
    row = mtx.shape[0]
    col = row
    
    for j in range(col):
        for i in range(j,row):
            if(i==j):
                mtx[i]= mtx[i]/(mtx[i][j])
            else :
                operator = (mtx[i][j])
                mtx[i]= mtx[i] - operator*mtx[j]

    for j in reversed(range(1,col)):
        for i in reversed(range(j+1)):
            if(i==j):
                continue
            else:
                mtx[i] = mtx[i] - mtx[i][j]*mtx[j]

    result = mtx[:,(mtx.shape[1]-1)]  
    return result
    
A = np.array([  [4,-3,1],
                [-2,1,-3],
                [1,-1,2]], dtype=float)

b = np.array([[-8,-4,3]], dtype=float)
b = np.transpose(b)

result = guassJordan(A,b)
print(result)