import mysql.connector
import secrets

def generate_strong_password(length=12):
    characters = ''.join([chr(i) for i in range(33, 127)])
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def passRequirement(str):
    upper,lower,number,symbol = False, False, False, False
    if len(str) < 8:
        return False
    for s in str:
        if upper == True and lower == True and number == True and symbol == True:
            return True
        if s.isupper():
            upper = True
        elif s.islower():
            lower = True
        elif s.isnumeric():
            number = True
        elif not s.isalpha():
            symbol = True
    if upper == True and lower == True and number == True and symbol == True:
            return True
    return False

serverPassword = input("Enter database password here: ")
connection = mysql.connector.connect(host ='localhost', user = 'root', password = serverPassword,database = 'test')
my_cursor = connection.cursor()

def addPassword():
    email = input("Enter your email here: ")
    askForPassGeneration = input("Do you want to use a secure automatic generated password? Press 1 for YES, Press any other key for NO: ")
    if askForPassGeneration == '1':
        password = generate_strong_password()
        print(f"Your automatically generated password is : {password}")
    else:
        password = input("Enter your password here: ")
    while not passRequirement(password):
        print('Password did not meet requirements, enter at least eight character and must include one of all uppercase, lowercase, numeric and symbol')
        password = input("Enter your password here: ")

    website = input("Enter the URL here: ")
    my_cursor.execute("INSERT INTO Passwords(email,pass,website) VALUES (%s,%s,%s)",(email,password,website))
    connection.commit()

def getPassword():
    website = input("Enter the URL here: ")
    my_cursor.execute("SELECT email,pass FROM Passwords WHERE website = %s",(website,))
    l1 = []
    d1 = {}
    for i in my_cursor:
        l1.append(i)
        d1[i[0]] = i[1]
        email = i[0]
    if len(l1) == 0:
        print("Website not present in database.")
        return
    if len(l1) > 1:
        email = input("Enter your email here: ")
    if email not in d1:
        print("Email not present in database.")
        return
    print(f"Email: {email} \nPassword: {d1[email]}")

def editPassword():
    website = input("Enter the URL here: ")
    my_cursor.execute("SELECT website FROM Passwords")
    l1 = []
    for i in my_cursor:
        l1.append(i[0])
    if website not in l1:
        print("Website not present in database.")
        return
    askForPassGeneration = input("Do you want to use a secure automatic generated password? Press 1 for YES, Press any other key for NO: ")
    if askForPassGeneration == '1':
        password = generate_strong_password()
        print(f"Your automatically generated password is : {password}")
    else:
        password = input("Enter your password here: ")
    while not passRequirement(password):
        print('Password did not meet requirements, enter at least eight character and must include one of all uppercase, lowercase, numeric and symbol')
        password = input("Enter your new password here: ")
    my_cursor.execute("UPDATE Passwords SET pass = %s WHERE website = %s",(password,website))
    connection.commit()

def delPassword():
    website = input("Enter the URL here: ")
    my_cursor.execute("SELECT website FROM Passwords")
    l1 = []
    for i in my_cursor:
        l1.append(i[0])
    if website not in l1:
        print("Website not present in database.")
        return
    my_cursor.execute("DELETE FROM Passwords WHERE website = %s",(website,))
    connection.commit()

def delAllPassword():
    confirmation = input("Are you sure you want to DELETE all the Passwords, Press 1 to confirm. ")
    if confirmation == '1':
        my_cursor.execute("DELETE FROM Passwords")
        connection.commit()
    return

def showAllPasswords():
    my_cursor.execute("SELECT email,pass,website FROM Passwords")
    for i in my_cursor:
        print(f"Email: {i[0]} Password: {i[1]} Website: {i[2]}")

def functionCaller():    
    action = int(input("1 - Get password\n2 - Add new password\n3 - Edit old password\n4 - Delete password from database\n5 - Delete ALL password from database\n6 - SHOW ALL password from database\n"))
    if action == 1:
        getPassword()
    elif action == 2:
        addPassword()
    elif action == 3:
        editPassword()
    elif action == 4:
        delPassword()
    elif action == 5:
        delAllPassword()
    elif action == 6:
        showAllPasswords()
    else:
        print("Wrong input, please enter valid input: ")
        functionCaller()


functionCaller()