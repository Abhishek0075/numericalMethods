def newtons_method(func, deriv_func, x0, tol=1e-6, maxIter=100):

    x = x0

    for _ in range(maxIter):
        fx = func(x)
        dfx = deriv_func(x)

        if abs(fx) < tol:
            return x

        if dfx == 0:
            raise ValueError("Derivative is zero. Cannot continue.")

        x = x - fx / dfx
        
    raise RuntimeError("The method did not converge within the maximum number of iterations.")


def functn(x):
    return x ** 3 - x - 1

def example_deriv_func(x):
    return 3 * x ** 2 - 1

root = newtons_method(functn, example_deriv_func, 1.5)
print("Root approximation:", root)
