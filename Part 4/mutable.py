Shopping_list = ["milk",
                 "pasta",
                 "eggs",
                 "spam",
                 "bread",
                 "rice",
                 ]
another_list = Shopping_list
print(id(Shopping_list))
print(id(another_list))

Shopping_list += ["cookies"]
print(Shopping_list)
print(id(Shopping_list))
print(another_list)

a = b = c = d = e = f = another_list
print(a)

print("Adding cream")
b.append("cream")
print(Shopping_list)
print(c)
print(d)
# equivalent to below
# a = another_list
# b = another_list
# c = another_list
# d = another_list
# e = another_list
# f = another_list