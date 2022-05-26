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


def get_all_values():
    wafer_id = []
    coordinates = []
    device_id = ['LMZ']

    rootDir = "./data"
    for subdir, dirs, files in os.walk(rootDir):
        for file in files:
            file_name = file.split('_')
            if len(file_name) >= 7:
                wafer_id.append(file_name[1]) if file_name[1] not in wafer_id else wafer_id
                coordinates.append(file_name[2]) if file_name[2] not in coordinates else coordinates
    return [wafer_id, coordinates, device_id]
