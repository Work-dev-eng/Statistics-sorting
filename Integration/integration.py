def f(x):
    return x**2

def integrate(f, a, b, n):

    h = (b - a) / n
    total = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        total += f(a + i * h)

    return total * h

result = integrate(f, 0, 2, 1000)
print("Estimated integral:", result)
