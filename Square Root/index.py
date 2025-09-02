import math

def calculate_square_root_builtin(number):
  """Calculates the square root of a number using the built-in math.sqrt() function."""
  if number < 0:
    return "Cannot calculate square root of a negative number."
  else:
    return math.sqrt(number)

# Example usage
num = float(input("Enter a number: "))
result = calculate_square_root_builtin(num)
print(f"The square root of {num} is: {result}")