def menu():
 print ("Main menu\n") 
 print ("1 - Load Data")
 print ("2 - Process Data")
 print ("3 - Visualise Data")
 print ("4 - Save Data")
 print ("5 - Exit")

user_input = input()
if(user_input == "Load Data"): 
  print("You have chosen option number 1")
elif(user_input == "Process Data"):
  print("You have chosen option number 2")
elif(user_input == "Visualise Data"):
  print("You have chosen option number 3") 
elif (user_input == "Save Data"):
  print("You have chosen option number 4")
elif(user_input == "Exit"):
 print("You have chosen option number 5")
else :
  print ("None")
return

choice = menu()
print(choice)

 