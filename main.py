
def menu():
 print ("Main menu\n --------------") 
 print ("Load Data")
 print ("Process Data")
 print ("Visualise Data")
 print ("Save Data")
 print ("Exit")
 print()
 user_input = input("Which option do you choose?\n")
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
  print("None")


print(menu())
