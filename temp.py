import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

fhand=open(file_path)
#fname=input('Enter File name: ')
#fhand=open(fname)
letters={}
while True:
    char=fhand.read(1)  #why 1????
    if not char:
        break
    char.lower()
    if char>='a' and char<='z':
        letters[char]=letters.get(char,0)+1
max=list()
for k,v in letters.items():
    max.append((v,k))
for k,v in sorted(max,reverse=True):
    print(k,v)
