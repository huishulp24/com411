# Read in user data 
print("What is your name human?")
name=input()
print("What is your age?")
age = int(input())
print("What is your weight?")
weight=float(input())
print("what is your height?")
height=float(input())
# Calculate bmi
bmi=weight/(height**2)
# Display result
print(name, "your bmi is:", (round (bmi, 2)))



