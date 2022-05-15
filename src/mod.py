import os

arr = os.listdir("C:/Users/main/Desktop/first/Project1/data")

print("\n".join(arr))

for (root, dirs, file) in os.walk("C:/Users/main/Desktop/first/Project1/data"):
    for f in file:
        print(f)
