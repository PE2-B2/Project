import os

arr = os.listdir("C:/Users/main/Desktop/first/Project1/data")


def call_dir(tag, caller):
    fileName = []
    for (root, dirs, file) in os.walk("C:/Users/main/Desktop/first/Project1/data"):
        for f in file:
            now = str(f)
            if now.find(caller) != -1:
                fileName.append(str(root) + '\\' + now)

    newFileName = []
    for fname in fileName:
        if fname.find(tag) != -1:
            newFileName.append(fname)
    return newFileName
