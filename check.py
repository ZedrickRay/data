import os

path = "C:\\Users\\edgar\\Desktop\\data\\labels\\Class A\\train"
path = "C:\\Users\\edgar\\Desktop\\data\\labels\\Class A\\val"
path = "C:\\Users\\edgar\\Desktop\\data\\labels\\Class B\\train"
path = "C:\\Users\\edgar\\Desktop\\data\\labels\\Class B\\val"
for f in os.listdir(path):
    if f.endswith(".txt"):
        lines = open(os.path.join(path, f)).read().strip().splitlines()
        for i, line in enumerate(lines):
            cols = len(line.strip().split())
            if cols != 38:
                print(f"{f} line {i+1}: {cols} columns (expected 38)")
