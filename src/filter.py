import os
from . import model

arr = os.listdir("./data")


def call_dir(tag, caller, coordinate):
    filename = []
    for (root, dirs, file) in os.walk("./data"):
        for f in file:
            now = str(f)
            if now.find(caller) != -1:
                filename.append(str(root) + '\\' + now)

    for fname in filename:
        if fname.find(tag) != -1 and fname.find(coordinate) != -1:
            return fname


def call_all_dir(tag, caller):
    filename = []
    for (root, dirs, file) in os.walk("./data"):
        for f in file:
            now = str(f)
            if now.find(caller) != -1:
                filename.append(str(root) + '\\' + now)

    newfilename = []
    for fname in filename:
        if fname.find(tag) != -1:
            newfilename.append(fname)
    return newfilename


def fileSplicer(pivot):
    wafer = ''
    coordinate = ''

    for t in model.waferId:
        if pivot.find(t) != -1:
            wafer = t

    flag = False
    for i in pivot:
        if flag == True or i == '(':
            coordinate = coordinate + i
            flag = True

        if i == ')':
            break
    return wafer, coordinate

