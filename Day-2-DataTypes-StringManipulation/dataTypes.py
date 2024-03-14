# How to determine the data type of a variable in python
a = 12  # this is a number
b = "string"  # this is a string
c = True  # this is a boolean
d = [1, 2, 3]  # this is a list


# write a function to determine the type of the variable
def findDataType(variable):
  typeOfVariable = type(variable)
  return typeOfVariable


print(findDataType(a))
print(findDataType(b))
print(findDataType(c))
print(findDataType(d))
