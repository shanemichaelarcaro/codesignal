def addBorder(picture):
    for index, value in enumerate(picture):
        picture[index] = "*" + value + "*"
    picture.append("*" * len(picture[0]))
    picture.insert(0, "*" * len(picture[0]))
    return picture

print(addBorder(["abc", "deb"]))