"""
import logic

print(logic.likes)
print(logic.comments)

print(logic.addlikes())

print(logic.addcomments("good"))  
print(logic.addcomments("nice"))  

"""
"""
from logic import addlikes, addcomments, likes, comments

print(likes)
print(comments)

print(addlikes())
print(addcomments("good"))

"""
"""
import logic as lg

print(lg.likes)
print(lg.comments)

print(lg.addlikes())
print(lg.addcomments("good"))

"""

# CASE 1

import logic

print(logic.add(10,5))
print(logic.sub(10,5))
print(logic.mul(10,5))
print(logic.div(10,5))
print(logic.mod(10,5))


#CASE 2 

import logic as lg

print(lg.add(10,5))
print(lg.sub(10,5))
print(lg.mul(10,5))
print(lg.div(10,5))
print(lg.mod(10,5))

#CASE 3

from logic import *

print(add(10,5))
print(sub(10,5))
print(mul(10,5))
print(div(10,5))
print(mod(10,5))

#CASE 4

from logic import add, sub, mul, div, mod

print(add(10,5))
print(sub(10,5))
print(mul(10,5))
print(div(10,5))
print(mod(10,5))
