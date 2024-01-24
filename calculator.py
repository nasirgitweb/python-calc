# Nasir-Calculator-Project
# Credit goes to nasir

# 1 . ADD
# 2 . SUBTRACT
# 3 . MULTIPLY
# 4 . DIVIDE

print("Select an operation to perform:")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")

operation = input()

#code_for_add_(made-by-nasir)
if operation == "1":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("the sum is " +  str(int(num1) + int(num2)))

#code_for_subtract_(made-by-nasir)
elif operation == "2":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("the result is " + str(int(num1) - int(num2)))

#code_for_multiply_(made-by-nasir)
elif operation == "3":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("the result is " + str(int(num1) * int(num2)))

#code_for_divide_(made-by-nasir)
elif operation == "4":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("the result is " + str(int(num1) / int(num2)))
    
else:
    print("Invalid Number Diso Bro, jao hege aso")


# ______________________THE END_______________________