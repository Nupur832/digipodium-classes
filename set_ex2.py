A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use | operator
print(A | B)

# use union function
A.union(B)

# use union function on B
B.union(A)

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A & B)

A.intersection(B)

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
# use - operator on A
print(A - B)
# use difference function on A
A.difference(B)
# use - operator on B
B - A
print(B - A)

print(A ^ B)
# use symmetric_difference function on A
A.symmetric_difference(B)