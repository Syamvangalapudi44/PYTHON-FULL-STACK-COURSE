# Normal function
"""
def wish(name):
    return f"Hello {name} , welcome to pfs"


"""
#Lambda Function 
"""
wishl = lambda name:f"Welcome {name}"

print(wishl("Tarun"))


"""
"""
add = lambda x , y : x+y
print(add(1,2))


multiple=lambda a,b: a*b
print(multiple(2,3))

even_or_odd = lambda a: "EVEN " if a%2==0 else "ODD"
print(even_or_odd(34))


compare = lambda a,b:"Greater" if a>b else "Smaller"
print(compare(1,2))

prices = ["$12.99","$29.99","$25.55"]
print(list(map(lambda p: float(p.replace("$","")), prices)))

l=["syam","tarun","vangalpudi"]
res = list(map(lambda name:name.title(),l))
print(res)

num=[20,40,50,80]
res=list(filter(lambda i : i % 20 ==0,num))
print(res)

num1 = list(map(int, input("enter number:")))
res = list(filter(lambda i: i % 2 == 0, num1))
print(res)
"""

from functools import reduce

nums = [1,2,3,4,5,6,7,8,9,10,8,2,8,5,3,2,1]

res = reduce(lambda a, b: a * b, nums)
print(res)