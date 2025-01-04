# 1) Len()
#The len() function in Python is used to determine the number of items in 
# an object. 

l = [10, 20, 30, 40, 50]
length = len(l)
print("Length is: ",length)

#2) Greet()
def greet():
    name=input("Enter your name: ")
    print("Hello", name)  
greet()

# 3) Max()
numbers = [3, 1, 7, 2, 5]
def find_maximum(numbers):
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum
result = find_maximum(numbers)
print("The maximum value is:", result)

# 4) Local and global variables
# Local Variables:
# ================
# *Defined inside a function.
# *Their scope is limited to the function where they are defined.
# *They are created when the function is called and destroyed when the 
#  function ends.

# Global Variables:
# ==================
# *Defined outside all functions and have a global scope.
# *Can be accessed and modified inside a function using the global keyword.
# *They exist throughout the program's execution.

a = 1000 # global variable

def verify():
    a = 200 # local variable
    print("Local variable is:", a)

verify()

print("Global variable is:", a)

# 5) Area()
def calculate_area(length, width=5):
    return length * width

area_with_width = calculate_area(50,3)
print("Area with both length and width given:", area_with_width)

area_without_width = calculate_area(50)
print("Area with only length given: ", area_without_width)










