#Recursive Function is nothing but a function is call by itself

def printing(n):
    if n >10 :
        return
    print(n)
    printing(n+1)
printing(1)

"""
"""
#reverse order---------
"""
def printing(n):
    if n >10 :
        return
    printing(n+1)
    print(n)
printing(1)
"""

#printing python programming
"""
def display(s,i):
    if i == len(s):
        return
    print(s[:i+1])
    display(s,i+1)
display("python programming",0)

"""
"""
def display(s,i):
    if i <= 0:
        return
    display(s,i-1)
    print(s*i)
display("abc",5)

"""

#list float str set tuple list dict

def display(n):
    n=n+10
    print("inside:",n)
n=10  
display(n)
print("outside",n)

      