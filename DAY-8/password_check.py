"""
def check_password(password):
    upper = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    lower = set("abcdefghijklmnopqrstuvwxyz")
    digits = set("0123456789")
    special = set("@#$%^&*!")
    p = set(password)
    if len(password) < 8:
        return "Invalid: Password must be at least 8 characters"
    
    if not p & upper:
        return "Invalid: Must contain uppercase letter"
    
    if not p & lower:
        return "Invalid: Must contain lowercase letter"
    
    if not p & digits:
        return "Invalid: Must contain digit"
    
    if not p & special:
        return "Invalid: Must contain special character"
    
    return "Valid Password "

password = input("Enter password: ")
print(check_password(password))


"""
"""

password=input("enter your password:")
check = set ()
if len(password) >= 8:
    for i in password:
        if i.islower():
            check.add("l")
        elif i.isupper():
            check.add("u")
        elif i.isdigit():
            check.add("d")
        else:
            check.add("s")
    if len(check)==4:
        print("strong password")

    else:
        print("weak password")
else:
    print("password is weak")

"""


password = input("Enter the password:  ")
check = set()
if len(password) >= 8:
    for i in password:
        if i.islower():
            check.add('l')
        elif i.isupper():
            check.add('u')
        elif i.isdigit():
            check.add('n')
        else:
            check.add('s')

    if len(check) == 4:
        print("strong password")
    else:
        print("weak password")

else:
    print("weak password")