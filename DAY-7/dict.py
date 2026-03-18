"""
data={"name":"tarun","age":21,"course":"PFS","skills":"python","college":"cmr","branch":"ece"}
print(data["branch"])

data["year"]=4
print(data)

data["address"]="hyderabad"
print(data)

sorted_data = dict(sorted(data.items()))  #for keys 
print(sorted_data)

del data["age"]
print(data)

data.popitem()
print(data)

"""

# Initial Dictionary
data = {
    "name": "tarun",
    "age": 21,
    "course": "PFS",
    "skills": "python",
    "college": "cmr",
    "branch": "ece"
}

print("Original Dictionary:", data)


# 🔑 Access
print("\nAccess name:", data["name"])


# ➕ Add
data["year"] = 4
print("\nAfter Adding year:", data)


# 🔄 Update
data["age"] = 22
print("\nAfter Updating age:", data)


# ❌ Delete using del
del data["skills"]
print("\nAfter Deleting skills:", data)


# ❌ Delete using pop
data.pop("course")
print("\nAfter Popping course:", data)


# 🔍 Check key
print("\nIs 'name' present?", "name" in data)


# 🔁 Loop
print("\nLooping through dictionary:")
for key, value in data.items():
    print(key, ":", value)


# 📊 Length
print("\nLength of dictionary:", len(data))


# 📋 Keys, Values, Items
print("\nKeys:", data.keys())
print("Values:", data.values())
print("Items:", data.items())


# 🔃 Copy
new_data = data.copy()
print("\nCopied Dictionary:", new_data)


# 🔀 Sorting by keys
sorted_keys = dict(sorted(data.items()))
print("\nSorted by Keys:", sorted_keys)


# 🔀 Sorting by values (safe)
sorted_values = dict(sorted(data.items(), key=lambda x: str(x[1])))
print("\nSorted by Values:", sorted_values)


# 🧹 Clear dictionary (uncomment to test)
# data.clear()
# print("\nAfter Clear:", data)

data={
    '123456':{'pin':'1234','balance':4000,'history':[]},
    '234561':{'pin':'1234','balance':6000,'history':[]},
    '345612':{'pin':'1234','balance':8000,'history':[]},
    '456123':{'pin':'1234','balance':9000,'history':[]},
    }

def deposit(acc_num):
    print('--------------------------------------------')
    amount = int(input("Enter the amount: "))
    data[acc_num]['balance']+=amount
    print(f"{amount} is deposited successfully")
    check_balance(acc_num)
    data[acc_num]['history'].append(f"{amount} is deposited")
    print('--------------------------------------------')

    
def withdraw(acc_num):
    print('--------------------------------------------')
    amount = int(input("Enter the amount: "))
    if data[acc_num]['balance'] >= amount:
        data[acc_num]['balance']-=amount
        print(f"{amount} is withdraw successfully")
        check_balance(acc_num)
        data[acc_num]['history'].append(f"{amount} is withdraw")
        print('--------------------------------------------')
    else:
        print("Insuffient balance")

    
def change_pin():
    pass

def check_balance(acc_num):
    print('--------------------------------------------')
    print(f"Current Balance: {data[acc_num]['balance']}")
    print('--------------------------------------------')


def view_transactions(acc_num):
    if data[acc_num]['history']:
        print("-------Transaction History-----------")
        for i in data[acc_num]['history']:
            print(i)
        else:
            print("--------------End of the transactions---------")
    else:
        print("No Transactions")

def menu():
    print("[C]heck Balance")
    print("[D]eposit")
    print("[W]ithdraw")
    print("[V]iew Transactions")
    print("Change [P]in")
    print("[E]xit")




print("-----------Welcome to the ATM-----------")
acc_num = input("Enter the account number: ")
pin = input("Enter the pin: ")

if acc_num in data and data[acc_num]['pin']==pin:
    print("Login Successful")
    while True:
        menu()
        ch = input("Enter your choice: ").lower()
        if ch=='c':
            check_balance(acc_num)
        elif ch=='d':
            deposit(acc_num)
        elif ch=='w':
            withdraw(acc_num)
        elif ch=='v':
            view_transactions(acc_num)
        elif ch=='p':
            change_pin(acc_num)
        elif ch=='e':
            print("--------Thankyou----------")
            break
        else:
            print("Enter the valid choice")

else:
    print("Invalid Login")








     