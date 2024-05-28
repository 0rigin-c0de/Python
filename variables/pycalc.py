print("Enter the first number: ")
num1 = float(input())

print("Enter an Operation(-, +, /, *):")
operation = input()

print("Enter the second number: ")
num2= float(input())

if operation == '+':
  result = num1 + num2
  print("The result is: ", result)
elif operation == '-':
  result= num1-num2
  print("The result is: ", result)
elif operation == '*':
  result =  num1*num2
  print("The result is: ", result)
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print("The result is:", result)
    else:
        print("Error: Division by zero is not allowed.")
else: 
   print("Invalid operation. Please enter one of +, -, /, *")

   