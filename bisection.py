def bisection_method(func, a, b, tol=1e-6, max_iter=100):
    
    if func(a) * func(b) >= 0:
        raise ValueError("The function must have opposite signs at the interval endpoints.")
    
    for i in range(max_iter):
        c = (a + b) / 2

        if abs(func(c)) < tol:
            return c

        if func(c) * func(a) < 0:
            b = c
        else:
            a = c
            
    raise RuntimeError("The method did not converge within the maximum number of iterations.")

def functn(x):
    return x ** 3 - x - 1

root = bisection_method(functn, 1, 2)
print("Root approximation:", root)
