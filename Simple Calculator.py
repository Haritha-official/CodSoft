#Designing a Simple Calculator

#Function for addition
def add(num1, num2):
    total = num1 + num2
    print("Sum is:",total)
#Function for subtraction
def sub(num1, num2):
    diff = num1 - num2
    print("Difference is:",diff)
#Function for multiplicaton
def mul(num1, num2):
    pro = num1 * num2
    print("Product is:",pro)
#Function for division
def div(num1, num2):
   if num2 != 0:
     result = num1 / num2
     print("Result:", result)
   else:
       print("Error: Division by zero!")
#Function for modulus
def modulo(num1, num2):
    remain = num1 % num2
    print("Remainder is:",remain)
#Function for square
def sqr(num1):
    squr = num1 * num1
    print("Square is:",squr)
#Welcome message
print("\n WELCOME, ASK WHAT YOU WANT!")
#Arithematic Operations
while True:
          print("\n Select the Operation")
          print("\n1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n5. Modulus \n6. Square \n7. Quit")
#Getting choice from the user
          choice = input("\n Enter your choice:")

          if(choice == "1"):
            num1 = float(input("Enter num1:"))
            num2 = float(input("Enter num2:"))
            add(num1, num2)
          elif(choice == "2"):
              num1 = float(input("Enter num1:"))
              num2 = float(input("Enter num2:"))
              sub(num1, num2)
          elif(choice == "3"):
              num1 = float(input("Enter num1:"))
              num2 = float(input("Enter num2:"))
              mul(num1, num2)
          elif(choice == "4"):
              num1 = float(input("Enter num1:"))
              num2 = float(input("Enter num2:"))
              div(num1, num2)
          elif(choice == "5"):
              num1 = float(input("Enter num1:"))
              num2 = float(input("Enter num2:"))
              modulo(num1, num2)
          elif(choice == "6"):
              num1 = float(input("Enter num1:"))
              sqr(num1)
          elif(choice == "7"):
              break
          else:
              print("ERROR! INVALID INPUT")

        
    
