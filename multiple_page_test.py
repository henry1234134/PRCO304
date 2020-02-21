import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import _thread, time, datetime
import subprocess

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class Page1(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is page 1")
       label.pack(side="top", fill="both", expand=True)

class Page2(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)

       label = tk.Label(self, text="Nmap")
       label.pack(side=TOP)

       def button_press():

           if (entry.get() == ""):  # some basic validation
               entry_valid = False
           else:
               entry_valid = True

           # open('ping_scan_results_file', 'w').close()         possible use of clearing txt

           if(entry_valid == True):
               ping_scan = """
               ls
               nmap """ + get_scan_selected() + """ """ + entry.get() + """> ping_scan_results_file
               """

               # subprocess.call(["ls"], shell=True)

               txtResult.config(state=NORMAL)  # makes it editable to insert text
               txtResult.delete('1.0', END)  # deletes the previous scan
               txtResult.insert(INSERT, "Processing...")  # inserts text into the textbox
               txtResult.config(state=DISABLED)  # makes it uneditable again

               process1 = subprocess.Popen([ping_scan], shell=True)

               print(entry.get())

               process1.wait()  # waits for the process to finish

               file = open("ping_scan_results_file", "r")

               txt = file.read()

               txtResult.config(state=NORMAL)  # makes it editable to insert text
               txtResult.delete('1.0', END)  # deletes the previous scan
               txtResult.insert(INSERT, txt)  # inserts text into the textbox
               txtResult.config(state=DISABLED)  # makes it uneditable again

               file.close()  # terminates the resources in use


       entry = tk.Entry(self)  # makes a txt box for people to enter stuff
       entry.pack(side=BOTTOM)

       nmapimage = ImageTk.PhotoImage(Image.open("Images/nmap.png"))
       nmapimage.height()
       imagelbl = tk.Label(self, image=nmapimage)
       imagelbl.image = nmapimage
       imagelbl.pack(side=TOP, fill="both", expand="no")
       #imagelbl.place(x=0, y=0)

       txtResult = tk.Text(self, borderwidth=0, relief="flat", state=DISABLED)  # this is where text is displayed
       txtResult.pack()

       label1 = tk.Label(self, text="Host Discovery") # text
       label1.place(relx=0.025, rely=0.45, anchor=W)

       selection = IntVar()
       r1 = Radiobutton(self, text="List Scan", variable=selection, value=1)
       r1.place(relx=0.035, rely=0.5, anchor=W)

       r2 = Radiobutton(self, text="Ping Scan", variable=selection, value=2)
       r2.place(relx=0.035, rely=0.55, anchor=W)

       label2 = tk.Label(self, text="OS Detection")
       label2.place(relx=0.025, rely=0.60, anchor=W)

       r3 = Radiobutton(self, text="OS Detection", variable=selection, value=3)
       r3.place(relx=0.035, rely=0.65, anchor=W)

       label3 = tk.Label(self, text="Version Detection")
       label3.place(relx=0.025, rely=0.70, anchor=W)

       r4 = Radiobutton(self, text="Version Detection", variable=selection, value=4)
       r4.place(relx=0.035, rely=0.75, anchor=W)

       def get_scan_selected():
           if selection.get() == 1:
               x = "-sL"
               return x
           elif selection.get() == 2:
               x = "-sn"
               return x
           elif selection.get() == 3:
               x = "-O"
               return x
           elif selection.get() == 4:
               x = "-sV"
               return x
           else:                        # fixes the problem if no radio button was selected by making the first choice default
               x = "-sL"
               return x

       button = tk.Button(self, text="Initiate Scan", padx=10, pady=5, fg="white", bg="black", command = button_press)  # creates the button
       button.pack(side = "bottom")

class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is page 3")
       label.pack(side="top", fill="both", expand=True)

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)       # pages are classes
        p2 = Page2(self)
        p3 = Page3(self)

        buttonframe = tk.Frame(self) # where buttons are kept
        container = tk.Frame(self) # where pages are kept
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Home Page", command=p1.lift)
        b2 = tk.Button(buttonframe, text="Nmap", command=p2.lift)
        b3 = tk.Button(buttonframe, text="Page 3", command=p3.lift)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")

        txtDate = tk.Text(buttonframe, height=1, bg="white")
        txtDate.pack(side="right", expand="false")
        def insert_date_time(lol, delay):
            while True:
                time.sleep(delay)
                txtDate.config(state=NORMAL)
                txtDate.delete('1.0', END)  # clears previous text
                currentTime = datetime.datetime.now()
                currentTime = currentTime.strftime('%H:%M:%S')  # formatting time
                txtDate.insert(INSERT, currentTime)
                txtDate.config(state=DISABLED)  # not editable
        _thread.start_new_thread(insert_date_time, (None, 1))

        p1.show()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("EzPz Tools")
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.maxsize(1920, 1080)
    root.minsize(900, 600)
    root.mainloop()