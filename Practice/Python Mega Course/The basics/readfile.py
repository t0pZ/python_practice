myfile = open("files/fruits.txt")
content = myfile.read()

print(content)

with open("files/fruits.txt") as myfile:
    content = myfile.read()

print(content)