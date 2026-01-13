# Write a function that takes a number n and prints the factorial of nef factorial(n):
 result = 1
 for i in range(1, n + 1):
 result *= i
 return result
num = int(input("Enter a number: "))
print(f"The factorial of {num} is {factorial(num)}")