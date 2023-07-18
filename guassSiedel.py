def gauss_seidel(A, b, max_iter=100, tol=1e-6):
    n = len(A)
    x = [0, 0, 0]
    for count in range(max_iter):
        x_prev = x.copy()
        for i in range(n):
            sigma = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x[i] = (b[i] - sigma) / A[i][i]
        if max(abs(x[i] - x_prev[i]) for i in range(n)) < tol:
            break
    return x

A =[[4, 1, -1],
    [2, 7, 1],
    [1, -3, 12]]

b = [3, 19, 31]

solution = gauss_seidel(A, b)
print("Solution:", solution)
