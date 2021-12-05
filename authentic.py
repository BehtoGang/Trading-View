def checker(password):
    has_letter = False
    has_number = False
    for i in password:
        if i.isalpha():
            has_letter = True
        elif i.isnumeric():
            has_number = True
        if has_letter and has_number:
            return True
    return False


def register():
    db = open("database.txt", "r")
    Username = input("Create your username:")
    Password = input("Please Enter password for your account, and make sure it has at least one letter and one number:")
    Passwordc = input("Confirm your password:")
    d = []
    f = []
    
    for i in db:
        a,b = i.split(", ")
        b = b.strip()
        d.append(a)
        f.append(b)
    data = dict(zip(d, f))

    check = checker(Password)
    if Password != Passwordc:
        print("The second password you entered isn't match with the first one!")
        register()
    else:
        if len(Password)<8:
            print("Your password must be at least 8 letters")
            register()
        elif check == False:
            print("Make sure your password contains a letter and a number!")
            register()
        elif Username in d:
            print("This username exists")
            register()
        else:
            db = open("database.txt", "a")
            db.write(Username+", "+Password+"\n")
            print("Your username and password has been saved succesfully")  
    

def access():
    db = open("database.txt","r")
    Username = input("Enter your username:")
    Password = input("Please Enter your password :")

    if not len(Username or Password) <1:
        d = []
        f = []
    
        for i in db:
            a,b = i.split(", ")
            b = b.strip()
            d.append(a)
            f.append(b)
        data = dict(zip(d, f))
        

        try:
            if data[Username]:
                try:
                    if Password == data[Username]:
                        print("Login successful")
                        print("Hi,", Username,"welcome!")
                    else:
                        print("Username or Password is incorrect")
                        home()
                except:
                    print("incorrect Username or Password")
                    home()
            else:
                print("Username or Password doesn't exist")
                home()
        except:
            print("Username or Password doesn't exist")
            home()
    else:
        print("please enter a value")
        home()
                        
def home(option=None):
    option = input("login | signup:")
    if option == "login":
        access()
    elif option == "signup":
        register()
    else:
        print("Please enter a correct option")
home()


