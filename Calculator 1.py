# The Variable 'num1' is what is used to define the first number
num1 = int(input('What is your first Number: '))

# The Variable 'unit_of_operation' prompts the user on what they want to do to the number
unit_of_operation = input('What unit of operation do you want to use. + for addition, - for subtraction, * for multipication and / for divison: ')

# # The Variable 'num2' is what is used to define the second number
num2 = int(input('What is your second Number: ' ))


if unit_of_operation == '+':
    print('This is the result if your numbers were added.', num1 + num2,'.')
    
if unit_of_operation == '-':
    print('This is the result if your numbers were subtracted.', num1 - num2,'.')

if unit_of_operation == '*':
    print('This is the result if your numbers were multiplication.', num1 * num2,'.')

if unit_of_operation == '/':
    print('This is the result if your numbers were divided.', num1 / num2,'.')


