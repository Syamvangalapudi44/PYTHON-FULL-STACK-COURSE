
name=list(input("enter your name ").split('-'))
age=int(input("enter your age"))
price=float(input("enter the price :"))

#-------INT--------------
numbers=list(map(int,input("enter your numbers").split()))
numbers1=set(map(int,input("enter your numbers ").split()))
numbers2=tuple(map(int,input("enter your numbers").split()))

#--------FLOAT------------
numbers3=list(map(float,input("enter your numbers").split()))
numbers4=set(map(float,input("enter your numbers").split()))
numbers5=tuple(map(float,input("enter your numbers").split()))

print(numbers)
print(numbers1)
print(numbers2)
print(numbers3)
print(numbers4)
print(numbers5)
print(name)
print(age)
print(price)
print(type(age))
print(type(price))

#-------- arthemetic operators---------

a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
add=a+b
sub=a-b
multiply=a*b
divide=a/b
modulo=a/b
floor_div=a//b
print(add)
print(sub)
print(divide)
print(modulo)
print(floor_div)

#--------comparision onperators---------
print(a>b)
print(a<b)
print(a==b)
print(a!=b)
print(a==b)
print(a>=b)
print(a<=b)

#------logical operators----------
# AND ,OR ,NOT

print(a and b)
print(a or b)
print(not a)

a=[1.2,3,4,5,]
b=[1,2,3,4,5,] 
print()
c=id(a)
d=id(b)
print(c,d)