import os

arr = os.listdir("./data")


def call_dir(tag, caller, coordinate):
    filename = []
    for (root, dirs, file) in os.walk("./data"):
        for f in file:
            now = str(f)
            if now.find(caller) != -1:
                filename.append(str(root) + '\\' + now)

    newfilename = []
    for fname in filename:
        if fname.find(tag) != -1 and fname.find(coordinate) != -1:
            return fname
