import numpy as np

def guassSiedel(mtx,b,x, iterations=100, tolerance=0.005):
    n = len(mtx)
    m = 0
    
    for i in range(iterations):
        previous_x = x.copy()
        checker = [0,0,0]

        for i in (range(n)):
            row_values = mtx[i]
            x[i] = 0
            foundValue = sum(x*row_values)
            numerator = (b[i] - foundValue)
            denominator = mtx[i][i]
            solution =  numerator/denominator
            x[i] = solution
            
        m+=1
        checker = [abs(x[i]-previous_x[i]) for i in range(n)]
        if(all(value <= tolerance for value in checker)):
            print("Found at the iteration : ",m)
            print("Solution :",end="")
            return x
        
        
    print("After iterations ", iterations, "we got ")
    return x

A = np.array([  [2,-1,0],
                [-1,2,-1],
                [0,-1,2]])

b = np.array([7,1,1])

x = np.zeros(len(A))


solution = guassSiedel(A, b, x)

print(solution)
