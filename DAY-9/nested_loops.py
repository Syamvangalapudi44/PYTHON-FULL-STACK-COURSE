#----------------NESTED FOR LOPPS---------------------
"""
n=int(input("enter the no of rows you need:"))
for j in range(n):
    for i in range(6):
        print("*",end=" ")
    print()

"""
"""
n=int(input("enter the size:"))
for row in range(n):
    for col in range(n-row):
        print("*",end=" ")
    print()
"""
n=int(input("enter the size:"))
for row in range(n):
    for spc in range(n-row-1):
        print(" ",end=" ")
    for col in range(row+1):
        print("*",end=" ")
    print()

