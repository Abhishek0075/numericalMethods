import numpy as np

def solve(mtx,b): 
    (row,col) = mtx.shape
    final = np.zeros(row)
    
    for i in reversed(range(row)):
        foundValue = sum(final*mtx[i])
        numerator = (b[i] - foundValue)
        denominator = mtx[i][i]
        solution =  numerator/denominator
        final[i] = solution
        
    return final

def guassElimination(A,b):
    mtx = np.concatenate((A, b), axis=1)
    row = mtx.shape[0]
    col = mtx.shape[1]
    
    for j in range(col):
        for i in range(j,row):
            if(i==j):
                mtx[i]= mtx[i]/(mtx[i][j])
            else :
                operator = (mtx[i][j])
                mtx[i]= mtx[i] - operator*mtx[j]
                
    b = mtx[:,(mtx.shape[1]-1)]
    mtx = np.delete(mtx,(mtx.shape[1]-1),1)
    result = solve(mtx,b)

    return result
    
A = np.array([  [4,-3,1],
                [-2,1,-3],
                [1,-1,2]], dtype=float)

b = np.array([[-8,-4,3]], dtype=float)
b = np.transpose(b)

result = guassElimination(A,b)
print(result)