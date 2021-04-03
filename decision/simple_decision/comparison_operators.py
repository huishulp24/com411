# Ask user for a number 
print("Please enter the first number")
first_number = int(input())
print("Please enter a second number")
second_number = int(input())
if(first_number < second_number):
  print("\nFirst number is smallest!")
elif(first_number > second_number):
  print("The second is smallest!")
else:
    print("\nThe two numbers are equal.")

