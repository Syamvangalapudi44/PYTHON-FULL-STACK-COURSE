"""
# grocery store products with prices
products = {
    "Rice": 50,
    "Milk": 30,
    "Bread": 25,
    "Eggs": 6,
    "Sugar": 40
}
print("---- Grocery Store ----")

# print index, product and price
for i, item in enumerate(products):
    print(i, ":", item, "- Price:", products[item])

print("-----------------------")

total = 0

# ask quantity for each product
for item in products:
    qty = int(input(f"Enter quantity for {item}: "))
    price = products[item] * qty
    total += price

print("-----------------------")
print(f"{qty}*{price}={total}")
print("Total Bill =", total)
print("Thank you for shopping!")

"""

"""
products=["rice","wheatfloor","sugar","milk","jam","bread","salt","sugar","oil","eggs"]

prices=[100,30,40,30,10,35,25,10,45,60]

print("--------WELCOME TO OUR STORE----------")
print("here these are the acailable items :")
print("INDEX".ljust(6,' '),"products".ljust(12,' '),"prices".ljust(6,' '))

for i in range(10):
    print(str(i+1).ljust(8,' '),products[i].ljust(12,' '),str(prices[i]).ljust(9,' '))
items=list(map(int,input("enter your index value:").split()))

print("---selected items--------") 
total_amount=0
for item in items:
    print(products[item-1],prices[item-1])
    total_amount=prices[item-1]


"""






