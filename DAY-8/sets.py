#  ALL SET OPERATIONS IN ONE CODE

# 1. Creating sets
a = {1, 2, 3, 3}
b = set([3, 4, 5])

print("Set a:", a)
print("Set b:", b)

# 2. Adding elements
a.add(6)
a.update([7, 8])
print("After adding:", a)

# 3. Removing elements
a.remove(1)        # remove specific element
a.discard(10)      # no error if element not present
a.pop()            # removes random element
print("After removing:", a)

# 4. Set operations
print("Union:", a | b)
print("Intersection:", a & b)
print("Difference (a-b):", a - b)
print("Symmetric Difference:", a ^ b)

# 5. Comparison operations
x = {1, 2}
y = {1, 2, 3}

print("Subset:", x.issubset(y))
print("Superset:", y.issuperset(x))
print("Disjoint:", x.isdisjoint({4, 5}))

# 6. Copy
c = a.copy()
print("Copy of a:", c)

# 7. Membership and length
print("Is 2 in a?", 2 in a)
print("Length of a:", len(a))

# 8. Looping
print("Looping through set a:")
for i in a:
    print(i)

# 9. Built-in functions
print("Max:", max(a))
print("Min:", min(a))
print("Sum:", sum(a))
print("Sorted:", sorted(a))

# 10. Frozen set
fs = frozenset([10, 20, 30])
print("Frozen set:", fs)

# 11. Clear set
c.clear()
print("After clear:", c)



