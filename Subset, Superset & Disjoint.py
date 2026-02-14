# Set Operations in Python
# Subset, Superset, Disjoint Example

# Creating Sets
A = {1, 2, 3, 4}
B = {1, 2}
C = {5, 6}

print("Set A:", A)
print("Set B:", B)
print("Set C:", C)

# 1️⃣ Subset
print("\nIs B subset of A?")
print(B.issubset(A))     # True

# 2️⃣ Superset
print("\nIs A superset of B?")
print(A.issuperset(B))   # True

# 3️⃣ Disjoint
print("\nAre A and C disjoint?")
print(A.isdisjoint(C))   # True
