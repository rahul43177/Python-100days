name = "Rahul"
#iterating over the string and printing them using the indexes
print(name[0])
print(name[1])
print(name[2])


#type conversion 
# it will be clear by the below example ->
# Take two numbers from user as an input , but the input is by deafult in strings 
# convert those into int , and then pass the value to a function which returns their sum 

number1 = input("Please enter the first number \n")
number2 = input("Please enter the second number \n")

#converting the number1 and number2 into int 
number1 = int(number1)
number2 = int(number2)
#checking their type
print(type(number1))
print(type(number2))
#function to return the sum of the two numbers
def add(num1 , num2):
  return num1+num2

print(add(number1 , number2))