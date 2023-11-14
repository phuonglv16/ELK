f = open("abc/c.txt", "r")
fpos= f.tell()
print("doc toi vị tri", fpos)

line= f.readline()
print("line", end *"")

fpos= f.tell()
print("doc toi vị tri", fpos)