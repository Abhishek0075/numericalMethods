def fn(x):
    return x**2 - 4

def false_position_method(f, a, b, tolerance=1e-6, maxIterations=100):
    iterationNum = 0
    while iterationNum < maxIterations:
        c = ((a * fn(b)) - (b * fn(a))) / (fn(b) - fn(a))

        if abs(fn(c)) < tolerance:
            return c

        if fn(c) * fn(a) < 0:
            b = c
        else:
            a = c

        iterationNum += 1

root = false_position_method(fn, 0, 3)
print("Approximate root:", root)
