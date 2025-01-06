a = "John/nope::Jason/yep"
b = a.split("::")
c = []
for i in b:
    res = i.split("/")
    c.append(res)

print(a)
print(b)
print(c)
