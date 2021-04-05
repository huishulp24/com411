
def source_data_path():
    """
    Task 6: Retrieve a file path to the source data file.

    The function should prompt the user to enter the file path for a data file (e.g. 'data/sol_data.csv').
    If the file path entered by the user does not end in 'csv' then a suitable error message should be displayed
    and the value None should be returned.
    Otherwise, the file path entered by the user should be returned.

    :return: None if the file path does not end in 'csv' otherwise return the file path entered by the user
    """
    print("Please enter a file path fo a data file:")
    file_path = input()
    file_path = "csv"
    if( file_path == file_path "csv"):
      print()
    else:
      print("Error!")
      print("None")


#==========================================

def process_type():
    """
    Task 7: Display a menu of options for how the file should be processed. Read in the user's response.

    A menu should be displayed that contains the following options:
        'Retrieve entity', 'Retrieve entity details', 'Categorise entities by type',
        'Categorise entities by gravity', 'Summarise entities by orbit'

    The user's response should be read in and returned as an integer corresponding to the selected option.
    For example, 1 for 'Retrieve entity', 2 for 'Retrieve entity details' and so on.

    If the user enters a invalid option then a suitable error message should be displayed and the value
    None should be returned.

    :return: None if an invalid selection made otherwise an integer corresponding to a valid option
    """
def process_type():
 print ("Menu\n") 
 print ("'Retrieve entity'")
 print ("'Retrieve entity detail'")
 print ("'Categorise entities by type'")
 print ("'Categorise entities by gravity'")
 print ("'Summarise entities by orbit'")
 user_input = input()
if(user_input == 'Retrieve entity'):
  print("You have chosen option number 1")
elif(user_input == 'Retrieve entity detail'):
  print("You have chosen option number 2")
elif(user_input == 'Categorise entities by type):
  print("You have chosen option number 3") 
elif(user_input == 'Categorise entities by gravity'):
  print("You have chosen option number 4")
elif(user_input == 'Summarise entities by orbit):
  print("You have chosen option number 5")
else:
  print(return = "There is no such option!")


