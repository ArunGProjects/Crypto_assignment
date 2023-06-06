def extended_euclidean_algorithm(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_euclidean_algorithm(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y
a = 84
b = 18
gcd, x, y = extended_euclidean_algorithm(a, b)
print("GCD:", gcd)
print("Coefficients (x, y):", x, y)
