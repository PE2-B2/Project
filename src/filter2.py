import os

arr = os.listdir("C:/Users\82109\PycharmProjects\Project_B2\Project_B2\data")

filename = []
for (root, dirs, file) in os.walk("C:/Users\82109\PycharmProjects\Project_B2\Project_B2\data"):
    for f in file:
        now = str(f)
        if now.find('LMZ') != -1:
            # print (now)
            filename.append(now)

tag = str(input("Input wafer name : "))

for fname in filename:
    if fname.find(tag) != -1:
        print(fname)
