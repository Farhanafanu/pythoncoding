def fact(n):
    if n<1:
        return 1
    else:
        return n *fact(n-1)
result=fact(5)
print(result)
def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result = result * i
        return result

# Test the factorial function
result = factorial(5)
print(result)  # Output: 120 (5! = 5 * 4 * 3 * 2 * 1 = 120)
