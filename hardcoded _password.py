Username = input("Enter Username to Login !!")
Password = input("Enter Password for "+Username+" !!\n")

hard_password = "Open123"

if(Username == "Admin" and Password == hard_password):
    {
        print("Success !!! Welcome "+Username)
    }
else:
    {
        print("Incorrect credentials detected !!")
    }
    
