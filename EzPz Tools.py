import tkinter as tk
from tkinter import *
import os
import subprocess # To see the output
import time, datetime
import _thread

def host_discovery_scan():
    # open('ping_scan_results_file', 'w').close()         possible use of clearing txt
    ping_scan = """
    ls
    nmap """+get_scan_selected()+""" """+entry.get()+"""> ping_scan_results_file
    """

    # subprocess.call(["ls"], shell=True)

    process1 = subprocess.Popen([ping_scan], shell=True)

    print(entry.get())

    process1.wait() # waits for the process to finish

    file = open("ping_scan_results_file", "r")

    txt = file.read()

    txtResult.config(state=NORMAL) # makes it editable to insert text
    txtResult.delete('1.0', END) # deletes the previous scan
    txtResult.insert(INSERT, txt) # inserts text into the textbox
    txtResult.config(state=DISABLED) # makes it uneditable again

    file.close() # terminates the resources in use

root = tk.Tk()  # holds everything
root.title("EzPz Tools")
root.maxsize(1920,1080)
root.minsize(900,600)

canvas = tk.Canvas(root, height=700, width=700, bg="white") # root is where you want to attach the canvas
canvas.pack() # attaches it to the root

frame = tk.Frame(root, bg="white") # attaching divisions to the canvas
frame.place(relwidth=0.8, relheight=0.5, relx=0.1, rely=0.1) #placing of the division

frameScrollBar = tk.Scrollbar(frame)
frameScrollBar.pack(side = RIGHT, fill=Y)

txtResult = tk.Text(frame, borderwidth=0, relief="flat", state=DISABLED, yscrollcommand=frameScrollBar.set) # this is where text is displayed
txtResult.pack()

txtDate = tk.Text(canvas, height = 1, bg="white")
txtDate.pack()

def insert_date_time(lol, delay):
    while True:
        time.sleep(delay)
        txtDate.config(state=NORMAL)
        txtDate.delete('1.0',END) # clears previous text
        currentTime = datetime.datetime.now()
        currentTime = currentTime.strftime('%H:%M:%S') # formatting time
        txtDate.insert(INSERT, currentTime)
        txtDate.config(state=DISABLED) # not editable

_thread.start_new_thread(insert_date_time,(None,1)) # started a new thread for the time so it doesnt use up all resources, it has to use 2 arguments so None is used

button = tk.Button(root, text="Initiate Scan", padx=10, pady=5, fg="white", bg="black", command=host_discovery_scan) # creates the button
button.pack(side = BOTTOM)

entry = tk.Entry(root) # makes a txt box for people to enter stuff
entry.pack(side = BOTTOM)

selection=IntVar()
r1 = Radiobutton(root, text="List Scan", variable=selection, value=1)
r1.place(relx=0.05, rely=0.9, anchor=W)

r2 = Radiobutton(root, text="Ping Scan", variable=selection, value=2)
r2.place(relx=0.05, rely=0.95, anchor=W)

def get_scan_selected():
    if selection.get() == 1:
        x = "-sL"
        return x
    elif selection.get() == 2:
        x = "-sn"
        return x

root.mainloop() # make it run