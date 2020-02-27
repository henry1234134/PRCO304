import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import _thread, time, datetime
import subprocess

themecolour = '#6374A3'
toolbarcolour = "#32435E"

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class Page1(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="EzPz Tools.\n The all in one user friendly pentesting tool for Kali Linux. \n Created by Henry Kaminarides.")
       label.pack(side="top", fill="both", expand=True)

class Page2(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)

       side_panel = Frame(self, bg=themecolour)
       side_panel.pack(side="left", fill="both", expand=False)

       label = tk.Label(self, text="Nmap Output Screen")
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

       nmapimage = ImageTk.PhotoImage(Image.open("Images/nmap.png"))
       nmapimage.height()
       imagelbl = tk.Label(side_panel, image=nmapimage, bg=themecolour)
       imagelbl.image = nmapimage
       imagelbl.pack(side=TOP, fill="both", expand="no")
       #imagelbl.place(x=0, y=0)

       frameScrollBar = tk.Scrollbar(self)
       frameScrollBar.pack(side=RIGHT, fill=Y)

       txtResult = tk.Text(self, borderwidth=10, relief="ridge", state=DISABLED, wrap=WORD, yscrollcommand=frameScrollBar.set)  # this is where text is displayed
       txtResult.pack(fill="both", expand="yes")




       txtResult.config(state=NORMAL)  # makes it editable to insert text
       txtResult.insert(INSERT, '''
___________      __________          ___________           .__          
\_   _____/______\______   \________ \__    ___/___   ____ |  |   ______
 |    __)_\___   /|     ___/\___   /   |    | /  _ \ /  _ \|  |  /  ___/
 |        \/    / |    |     /    /    |    |(  <_> |  <_> )  |__\___ \ 
/_______  /_____ \|____|    /_____ \   |____| \____/ \____/|____/____  >
        \/      \/                \/                                 \/ 
       ''')  # inserts brand
       txtResult.config(state=DISABLED)  # makes it uneditable again

       label1 = tk.Label(side_panel, text="Host Discovery", bg=themecolour, fg="White", font="bold") # text
       label1.place(relx=0.025, rely=0.45, anchor=W)

       selection = IntVar()
       r1 = Radiobutton(side_panel, text="List Scan", variable=selection, value=1, bg='#B3F2FF', activebackground='#FFFFA6')
       r1.place(relx=0.035, rely=0.5, anchor=W)

       r2 = Radiobutton(side_panel, text="Ping Scan", variable=selection, value=2, bg='#B3F2FF', activebackground='#FFFFA6')
       r2.place(relx=0.035, rely=0.55, anchor=W)

       label2 = tk.Label(side_panel, text="OS Detection", bg=themecolour, fg="White", font="bold")
       label2.place(relx=0.025, rely=0.60, anchor=W)

       r3 = Radiobutton(side_panel, text="OS Detection", variable=selection, value=3, bg='#B3F2FF', activebackground='#FFFFA6')
       r3.place(relx=0.035, rely=0.65, anchor=W)

       label3 = tk.Label(side_panel, text="Version Detection", bg=themecolour, fg="White", font="bold")
       label3.place(relx=0.025, rely=0.70, anchor=W)

       r4 = Radiobutton(side_panel, text="Version Detection", variable=selection, value=4, bg='#B3F2FF', activebackground='#FFFFA6')
       r4.place(relx=0.035, rely=0.75, anchor=W)

       label4 = tk.Label(side_panel, text="Port Scan", bg=themecolour, fg="White", font="bold")
       label4.place(relx=0.025, rely=0.80, anchor=W)

       r5 = Radiobutton(side_panel, text="Port Scan (All ports)", variable=selection, value=5, bg='#B3F2FF', activebackground='#FFFFA6')
       r5.place(relx=0.035, rely=0.85, anchor=W)

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
           elif selection.get() == 5:
               x = ""
               return x
           else:                        # fixes the problem if no radio button was selected by making the first choice default
               x = "-sL"
               return x

       button = tk.Button(self, text="Initiate Scan", padx=10, pady=5, fg="white", bg="black", command = button_press)  # creates the button
       button.pack(side = "bottom")

       entry = tk.Entry(self)  # makes a txt box for people to enter stuff
       entry.pack(side=BOTTOM)

       entrylbl = tk.Label(self, text="Enter target IP")
       entrylbl.place(relx=0.435, rely=0.935)

       entryhelplbl = tk.Label(self, text="Scan a range: 192.168.0.1-10 \n Scan a subnet: 192.168.0.1/13")
       entryhelplbl.place(relx=0.70, rely=0.94)

class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="Metasploit")
       label.pack(side="top", fill="both", expand=True)

       metasploit_commands = '''
       ls > ms_results
       '''
       ms_process = subprocess.Popen([metasploit_commands], shell=True)

       #process1.wait()  # waits for the process to finish

       file = open("ms_results", "r")

       txt = file.read()
       print(txt)
'''
       txtResult.config(state=NORMAL)  # makes it editable to insert text
       txtResult.delete('1.0', END)  # deletes the previous scan
       txtResult.insert(INSERT, txt)  # inserts text into the textbox
       txtResult.config(state=DISABLED)  # makes it uneditable again
'''
       #file.close()  # terminates the resources in use


class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)       # pages are classes
        p2 = Page2(self)
        p3 = Page3(self)

        buttonframe = tk.Frame(self, bg=toolbarcolour) # where buttons are kept
        container = tk.Frame(self) # where pages are kept
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Home Page", command=p1.lift, bg=toolbarcolour, bd=0, fg="#FFFFFF")
        b2 = tk.Button(buttonframe, text="Nmap", command=p2.lift, bg=toolbarcolour, bd=0, fg="#FFFFFF")
        b3 = tk.Button(buttonframe, text="Metasploit", command=p3.lift, bg=toolbarcolour, bd=0, fg="#FFFFFF")

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")

        txtDate = tk.Text(buttonframe, height=1, bg="white", width=8)
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
    root.minsize(1100, 750)
    root.mainloop()