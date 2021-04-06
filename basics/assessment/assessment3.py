def welcome():
    welcome_string = 'Solar Record Management System'
    print("-" * len(welcome_string), end ="")
    print(welcome_string, "-" * len(welcome_string), end ="")

welcome()
#=================================
def started(operation = "'{operation}"):

 print(operation, "has started.'")

started("'{operation}")
#==============================================

def completed(operation = "'{operation}"):

 print(operation, "has completed.'")

completed("'{operation}")


#==============================================


def error(error_msg = "{error_msg}'"):

 print("'Error!",  error_msg)

error("{error_msg}'")



