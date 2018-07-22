with open("text.txt", "w") as f:
    f.write("Hello Python")

with open("text.txt", "r") as f:
    print(f.read())
