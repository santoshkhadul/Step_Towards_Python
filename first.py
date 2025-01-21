# Take input from the user
a = float(input("Enter the value for a: "))
b = float(input("Enter the value for b: "))

# Arithmetic Operations

# Addition
sum_result = a + b
print(f"Sum: {sum_result}")

# Subtraction
subtraction_result = a - b
print(f"Subtraction: {subtraction_result}")

# Multiplication
multiplication_result = a * b
print(f"Multiplication: {multiplication_result}")

# Division
if b != 0:  # Check to avoid division by zero
    division_result = a / b
    print(f"Division: {division_result:.2f}")  # Formatting to 2 decimal places
else:
    print("Division: Error (Division by zero is not allowed)")

# Floor Division
if b != 0:
    floor_division_result = a // b
    print(f"Floor Division: {floor_division_result}")
else:
    print("Floor Division: Error (Division by zero is not allowed)")

# Modulo
if b != 0:
    modulo_result = a % b
    print(f"Modulo: {modulo_result}")
else:
    print("Modulo: Error (Division by zero is not allowed)")

# Exponentiation (Power)
power_result = a ** b
print(f"Power: {power_result}")

# Comparison Operations

# Equal to operator
equal_to_result = a == b
print(f"a == b: {equal_to_result}")

# Not equal to operator
not_equal_to_result = a != b
print(f"a != b: {not_equal_to_result}")

# Greater than operator
greater_than_result = a > b
print(f"a > b: {greater_than_result}")

# Less than operator
less_than_result = a < b
print(f"a < b: {less_than_result}")

# Greater than or equal to operator
greater_or_equal_to_result = a >= b
print(f"a >= b: {greater_or_equal_to_result}")

# Less than or equal to operator
less_or_equal_to_result = a <= b
print(f"a <= b: {less_or_equal_to_result}")
