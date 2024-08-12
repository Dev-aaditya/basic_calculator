def add(num1, num2):
    return num1 + num2
 
def subtract(num1, num2):
    return num1 - num2
 
def multiply(num1, num2):
    return num1 * num2
 
def divide(num1, num2):
    return num1 / num2
 
print("Please s operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n")
 
 
s = int(input("Select operations form 1, 2, 3, 4 :"))



if s == 1:
    number_1 = int(input("enter first number = "))
    number_2 = int(input("enter second number = "))
    print(number_1, "+", number_2, "=")
    add(number_1, number_2)
 

elif s == 2:
    number_1 = int(input("Enter first number: "))
    number_2 = int(input("Enter second number: "))
    print(number_1, "-", number_2, "=",
    subtract(number_1, number_2))
 

elif s == 3:
    number_1 = int(input("Enter first number: "))
    number_2 = int(input("Enter second number: "))
    print(number_1, "*", number_2, "=",
    multiply(number_1, number_2))
    
 
elif s == 4:
    number_1 = int(input("Enter first number: "))
    number_2 = int(input("Enter second number: "))
    print(number_1, "/", number_2, "=",
    divide(number_1, number_2))
    

else:
    print("Invalid input")