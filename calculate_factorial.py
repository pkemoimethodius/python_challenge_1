def factorial(n):
    """Calculate factorial of a non-negative integer."""
    if n < 0:
        return "Factorial is not defined for negative numbers"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(5))  