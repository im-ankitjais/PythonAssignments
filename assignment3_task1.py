def calculate_factorial(num):
    if num < 2:
        return 1
    else:
        return num * (calculate_factorial(num-1))

x = input("Enter Number: ")
x = int(x)

result = calculate_factorial(x)
print("Factorial of", x, "is:", result)

