
def sum_n(n):
    if n == 1:          # Base case
        return 1
    else:               # Recursive case
        return n + sum_n(n - 1)

n = int(input("Enter the value of N: "))

result = sum_n(n)

print("Sum of first", n, "natural numbers is:", result)
