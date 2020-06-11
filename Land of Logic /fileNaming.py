def fileNaming(names):
    for index in range(len(names)):
        if names[index] in names[:index]:
            counter = 1
            while names[index] + "(" + str(counter) + ")" in names[:index]:
                counter += 1
            names[index] += "(" + str(counter) + ")"
    return names

print(fileNaming(["doc", "doc", "image", "doc(1)", "doc"])) # => ["doc", "doc(1)", "image", "doc(1)(1)", "doc(2)"]
