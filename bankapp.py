# This is a python program for online banking system

class Bank():
    __bankname = "PB&J Bank" 
    balance = 0
    __usercount = 0  # This attribute gives us Account number

    def __init__(s,name,pin,gender,Age):
        s.__name = name
        s.__pin = pin
        s.gender = gender
        s.age = Age
        Bank.__usercount += 1
        s.accountno = 123400 + Bank.__usercount 
        #concatenated usercount with some initial characters which are "branch no" and "bank no" to obtain legit Account Number

    def deposite(s,amount):
        s.amount = amount
        s.balance = s.balance + amount

    
    def withdraw(s,amount):
        s.amount = amount
        s.balance = s.balance - s.amount
        
    def transfer(s,recipient, amount):
        s.amt = amount
        s.recipient = recipient #recipient is an another object of class Bank 
        s.recipient.balance = s.recipient.balance + s.amt
        s.balance = s.balance - s.amt
            
    def viewbalance(s):
        return s.balance

    def getuserinfo(s):
        return f"\n Username: {s.__name} \n Account No: {s.accountno} \n Gender: {s.gender} \n Age: {s.age}"
    
    def getusername(s):
        return s.__name

    def getpin(s):
        return s.__pin

    def logindata(s):
        return[s.__name, s.__pin]


def main():
    users = {} # Empty dictionary
    while(True):
        print("WELCOME TO PB&J BANK".center(40,"-"))
        print("Digital Banking Service".center(40,"~"))
        print("\nUser wants to \n1. Create Account \n2. Login \n3. Exit")
        # Above is our main menu where user creates a bank account
        c = input("Enter your selection: ")

        if(c=="1"):
            while True :
                name = input("Enter Your Username: ").lower()
                if name.isalpha():
                          break
                print("invalid username")
            # This code above ensures the input for username is alphabets only
            pin = input("Set Your Password: ")
            while True :
                gender = input("Enter Your gender (F/M): ").lower()
                if gender.isalpha() and gender=="f" or gender=="m":
                    break
                print("invalid input")
            # This code above ensures gender input is alphabets and either "f" or "m".
            while True :
                Age = input("Enter Your Age: ")
                if Age.isnumeric()and 18<=int(Age)<100:
                    break
                print("Your Age should be 18 or above to create account. ")
            # This code above ensures Age input is numeric and above or equal to 18
            
            users[name] = Bank(name,pin,gender,Age) 
            #created an object of class Bank with all login attributes and giving it a key of name and adds this key_value pair to the dictionary "users" we created in beginning

        elif(c=="2"):
            name = input("Enter Your username: ")
            pin = input("Enter Your Password: ")
            # here user is logging in
            obj = users.get(name,0)
           # If username and password is right they are checked with elements of dictionary "users"
            if(obj==0)or obj.logindata()!=[name,pin]:
                print("\nNo Match Found\n")  # If username and passwprd wrong or doesnt exists prints "no match"
            else:
                print("\nAccess Granted!\n") #If username and password found in dictionary grants access and next menu
                while True:
                    print("\nUser wants to \n1. Deposite money \n2. withdraw money \n3. Transfer money \n4. View your Balance  \n5. View User Information \n6. Main Menu")
                    c = input("Enter Your Selection: ")

                    if(c=='1'):
                        amt = int(input("Enter the amount: "))
                        obj.deposite(amt)
                        print (f"\n Amount Deposited Successfully! \n Balance = {obj.balance}")
                        
                    elif(c=="2"):
                        amt = int(input("Enter the amount: "))
                        if(amt>obj.balance):
                            print(f"\n Insufficient balance.\n Current Balance = {obj.balance}")
                        elif (amt >= 100) and (amt <= obj.balance):
                            obj.withdraw(amt)
                            print (f"\n Amount Withdawn Successfully! \n Balance = {obj.balance}")
                        else:
                            print(f"\n Withdrawal amount cannot be less than 100. \n Current Balance = {obj.balance}")
                            
                    elif(c=="3"):
                        user_name =input("Enter reciepent's username : ")
                        amt = int(input("Enter the amount: "))
                        user = users.get(user_name,None) # Get method Fetches the given input username from dictionary if it exists there
                        if user is None:
                            print("User Not Found.") #If get method returns none username is not present in dictionary  
                            continue
                        if (amt > obj.balance):
                            print(f"\n Insufficient Balance. \n Current balance = {obj.balance}")
                        elif (amt >= 1) and (amt <= obj.balance):
                            obj.transfer(user,(amt))
                            print (f"\n Amount Transfered Successfully! \n Balance = {obj.balance}")
                        elif (amt < 1):
                            print(f"\n You cannot transfer amount less than 1. \n Current Balance = {obj.balance}")
                         # If username exists we check the validity of ammount that can be transfered based on available balance and transfer amount from balance of one account object to balance of another account object   
                    elif(c=="4"):
                        print(f"\n Current Balance = {obj.viewbalance()}")

                    elif(c=="5"):
                        print(f"{obj.getuserinfo()}")
                        
                    elif(c=="6"):
                            break # Return to main menu
                        
                    else:
                        print("\n Invalid Input, Try Again.\n")

        elif(c=="3"):
            e = input(f"Do You really want to exit ? Select(Y/N): ").lower()
            if(e=='y'):
                break
            else:
                continue
            
main()      

