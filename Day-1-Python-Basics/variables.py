number1 = int(input("Please enter the number \n"))

number2 = int(input("Please enter the number \n"))

sum = (number1+number2)

if isinstance(sum , str):
    print("This is invalid number , the number you have entered is a string , please enter a valid number")
else:
    print("The sum is "+str(sum))


print("Hello world!")



  