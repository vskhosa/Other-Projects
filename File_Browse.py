#FileUploadWidget(label='Browse', _dom_classes=('widget_item', 'btn-group'))
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()
fhand=open(file_path)

print(file_path)
#fname=input('Enter File name: ')
fhand=open(file_path)

input('press any key to exit')
