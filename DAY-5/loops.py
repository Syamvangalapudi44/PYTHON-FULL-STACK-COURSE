"""

a=int(input("enter your number:"))
while a<=20:
    print(a)
    a+=1
"""
"""
a=int(input("enter your number:"))
while a<=20:
    if a==5:
        break
    print(a)
    a+=1
"""
"""
bullets=int(input("enter your bullets:"))
while bullets>0:
    print(f"{bullets} are only left")
    bullets-=1
print("your game is over")

"""
#--------------candycrush game---------------
"""
candy=int(input("enter your number:"))
winning_move=24
while candy > 0:
    if candy==24:
        print("you win the move")
        break
    print(f"you have only {candy} left ")
    candy-=1
print("you candies are out so game over")

"""
#----------STuddent attendance report----------------

"""
data={}
n=int(input("enter no of student :"))
for i in range(n):
    name=input("enter the name:")
    data[name]=False
print(data)
for name in data:
    status=int(input(f"enter the {name} status (0=absent),(1=present):"))
    data[name]=bool(status)
print(data)

"""
#-------------indexing of the string------------  
n="syam tarun"
print(n[:5])
print(n.replace("tarun","naidu"))
print(n)
print(n.center(12,"-"))
