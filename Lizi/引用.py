a = 100
b = a

print(id(a))
print(id(b))

A = [11, 22, 33]
B = A

print(id(A))
print(id(B))

A.append(44)

print(A)
print(B)

# 任何只要牵扯到赋值等号的地方，统统都是引用。
