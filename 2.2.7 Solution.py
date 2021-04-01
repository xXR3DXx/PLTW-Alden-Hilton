# This program is created by Alden Hilton for 2.2.7 PLTW. If given code is used, please credit repectively.

import tkinter as tk
import os
import subprocess
from tkinter import *

boxcreated = 0
def pinglocal():
    global boxcreated
    # Adds an output box to GUI.
    proc=subprocess.Popen(("dig " + str(e1.get())), shell=True, stdout=subprocess.PIPE, )
    output=proc.communicate()[0]

    if boxcreated == 0:
        command_textbox = tk.Label(text = str(output), height= 36, width=150)
        command_textbox.pack()
        boxcreated = 1


root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
ping_btn = tk.Button(frame, padx = 10, pady = 10, text="PING", command=pinglocal)
ping_btn.pack()
ping_btn = tk.Label(frame, text="Check to see if a URL is up and active\n\n")
ping_btn.pack()
frame_URL = tk.Frame(root, padx = 10, pady=0,  bg="white") # change frame color
frame_URL.pack()

e1 = tk.Entry(frame_URL,  font=("comic sans", 14)) # change font
e1.pack(side=tk.LEFT)

frame = tk.Frame(root,  bg="black") # change frame color
frame.pack()

root.mainloop()

'''
### CREDIT TO https://stackoverflow.com/questions/49371575/print-subprocess-popen FOR TERMINAL TO VARIABLE SRIPT ###
import subprocess
proc=subprocess.Popen('echo "to stdout"', shell=True, stdout=subprocess.PIPE, )
output=proc.communicate()[0]
print (output)
'''
