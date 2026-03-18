data = {
    "Raju" : {"status": True, "python": 99, "mysql":90, "django":97},
    "Ravi" : {"status": True, "python": 70, "mysql":60, "django":50},
    "buvan": {"status": True, "python": 80, "mysql":70, "django":67},
    "venkat":{"status": True, "python": 59, "mysql":60, "django":47},
    "manoj":{"status": True, "python": 19, "mysql":20, "django":7},
    "hemanth":{"status": False,"python":None,"mysql":None, "django":None}
    }

name = input("enter a name : ")

if name in data:
    if data[name]["status"]:
        sum = data[name]['python'] + data[name]['mysql'] + data[name]['django']
        avg = sum/3
        if avg >= 90:
            print(f'congrats {name}, you are the first class')
        elif avg>= 75:
            print(f' Good {name} , wish you all the best')
        elif avg>= 50:
            print(f'  {name}, need improvement')
        elif avg>=35:
            print(f'bad {name}, Word hard next time')
        else:
            print(f' {name}, you failed the exam')
    else:
        print(f' {name}, you have not written the exams. please bring your parents')

else:
    print(f' {name} not found in data')