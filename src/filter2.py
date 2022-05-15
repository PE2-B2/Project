import os

arr = os.listdir("C:/Users/main/Desktop/first/Project1/data")

filename = []
for (root, dirs, file) in os.walk("C:/Users/main/Desktop/first/Project1/data"):
    for f in file:
        now = str(f)
        if now.find('LMZ') != -1:
            # print (now)
            filename.append(now)

tag = str(input("Input wafer name : "))

for fname in filename:
    if fname.find(tag) != -1:
        print(fname)
