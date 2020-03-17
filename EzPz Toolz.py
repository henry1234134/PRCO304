import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import _thread, time, datetime
from subprocess import PIPE
import subprocess
import os, sys

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

        logo = ImageTk.PhotoImage(Image.open("Images/EzPz Toolz Logo.png"))
        imagelbl = tk.Label(self, image=logo)
        imagelbl.image = logo
        imagelbl.pack()


class Page2(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        side_panel = Frame(self, bg=themecolour)
        side_panel.pack(side="left", fill="both", expand=FALSE)

        label = tk.Label(self, text="Nmap Output Screen")
        label.pack(side=TOP)

        def button_press():

            if (entry.get() == ""):  # some basic validation
                entry_valid = False
            else:
                entry_valid = True

            # open('ping_scan_results_file', 'w').close()         possible use of clearing txt

            if (entry_valid == True):
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
        imagelbl = tk.Label(side_panel, image=nmapimage, bg=themecolour)
        imagelbl.image = nmapimage
        imagelbl.pack(side=TOP, fill="both", expand="no")
        # imagelbl.place(x=0, y=0)

        frameScrollBar = tk.Scrollbar(self)
        frameScrollBar.pack(side=RIGHT, fill=Y)

        txtResult = tk.Text(self, borderwidth=10, relief="ridge", state=DISABLED, wrap=WORD,
                            yscrollcommand=frameScrollBar.set)  # this is where text is displayed
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

        label1 = tk.Label(side_panel, text="Host Discovery", bg=themecolour, fg="White", font="bold")  # text
        label1.place(relx=0.025, rely=0.45, anchor=W)

        selection = IntVar()
        r1 = Radiobutton(side_panel, text="List Scan", variable=selection, value=1, bg='#B3F2FF',
                         activebackground='#FFFFA6')
        r1.place(relx=0.035, rely=0.5, anchor=W)

        r2 = Radiobutton(side_panel, text="Ping Scan", variable=selection, value=2, bg='#B3F2FF',
                         activebackground='#FFFFA6')
        r2.place(relx=0.035, rely=0.55, anchor=W)

        label2 = tk.Label(side_panel, text="OS Detection", bg=themecolour, fg="White", font="bold")
        label2.place(relx=0.025, rely=0.60, anchor=W)

        r3 = Radiobutton(side_panel, text="OS Detection", variable=selection, value=3, bg='#B3F2FF',
                         activebackground='#FFFFA6')
        r3.place(relx=0.035, rely=0.65, anchor=W)

        label3 = tk.Label(side_panel, text="Version Detection", bg=themecolour, fg="White", font="bold")
        label3.place(relx=0.025, rely=0.70, anchor=W)

        r4 = Radiobutton(side_panel, text="Version Detection", variable=selection, value=4, bg='#B3F2FF',
                         activebackground='#FFFFA6')
        r4.place(relx=0.035, rely=0.75, anchor=W)

        label4 = tk.Label(side_panel, text="Port Scan", bg=themecolour, fg="White", font="bold")
        label4.place(relx=0.025, rely=0.80, anchor=W)

        r5 = Radiobutton(side_panel, text="Port Scan (All ports)", variable=selection, value=5, bg='#B3F2FF',
                         activebackground='#FFFFA6')
        r5.place(relx=0.035, rely=0.85, anchor=W)

        def get_scan_selected():
            if selection.get() == 1:
                x = "-sL"
                return x
            elif selection.get() == 2:
                x = "-sP"
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
            else:  # fixes the problem if no radio button was selected by making the first choice default
                x = "-sL"
                return x

        button = tk.Button(self, text="Initiate Scan", padx=10, pady=5, fg="white", bg="black",
                           command=button_press)  # creates the button
        button.pack(side="bottom")

        entry = tk.Entry(self)  # makes a txt box for people to enter stuff
        entry.pack(side=BOTTOM)

        entrylbl = tk.Label(self, text="Enter target IP")
        entrylbl.place(relx=0.435, rely=0.935)

        entryhelplbl = tk.Label(self, text="Scan a range: 192.168.0.1-10 \n Scan a subnet: 192.168.0.1/13")
        entryhelplbl.place(relx=0.70, rely=0.94)


class Page3(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        # the initiation of metasploit on startup
        msfconsole_commands = ''' 
       msfconsole

        '''
        open('/root/msf_output.txt', 'w').close()  # deletes previous log file created
        p1 = subprocess.Popen(msfconsole_commands, stdin=PIPE, shell=True, text=True)
        p1.stdin.write('spool /root/msf_output.txt\n')  # redirects output of metasploit to a text file
        p1.stdin.flush()

        sidebarframe = tk.Frame(self, bg=themecolour)
        sidebarframe.pack(fill=BOTH, side=LEFT, expand=FALSE)

        msimage = ImageTk.PhotoImage(Image.open("Images/metasploit.png"))
        # msimage.height()
        imagelbl = tk.Label(sidebarframe, image=msimage, bg=themecolour)
        imagelbl.image = msimage
        imagelbl.pack(side=TOP, fill="both", expand="no")

        outputframe = tk.Frame(self)
        outputframe.pack(fill=BOTH, side=TOP, expand=TRUE) # used for the list of vulnerabilities

        inputframe = tk.Frame(self)
        inputframe.pack(fill=BOTH, side=BOTTOM, expand=FALSE)

        optionsframe = tk.Frame(self)  # frame inside sidebar frame used to contain and remove exploit options
        optionsframe.pack(fill=BOTH, expand=FALSE)

        # buttonsframe = tk.Frame(self)
        # buttonsframe.pack(fill=BOTH, expand=TRUE)

        # txtbox = tk.Text(outputframe, wrap=WORD, yscrollcommand=frameScrollBar.set)
        # txtbox.pack(fill="both")

        frameScrollBar = tk.Scrollbar(outputframe)
        frameScrollBar.pack(side=RIGHT, fill=Y)

        lstbox = tk.Listbox(outputframe, yscrollcommand=frameScrollBar.set)
        lstbox.pack(side=LEFT, fill=BOTH, expand=TRUE)
        # L = lstbox.curselection()

        entry = tk.Entry(inputframe)
        entry.pack()

        def search_vulns():
            open('/root/msf_output.txt', 'w').close()  # deletes previous log file created
            # txtbox.delete('1.0', END)  # deletes the previous scan
            exploit_list = list()  # instantiates list of exploits
            count = 1  # number used for adding to listbox
            lstbox.delete(0, tk.END)  # clears the listbox of the previous scan

            p1.stdin.write('search platform:' + entry.get() + '\n')  # specifying search
            p1.stdin.flush()  # clears the previous input
            time.sleep(2)  # gives time for it to be written to file

            with open('/root/msf_output.txt', "r") as lines:  # edits the output
                for line in lines:
                    if line.find("exploit") > 0:  # prevents the next line being taken for the next iteration
                        num = int(line.find("exploit"))  # searches for the index of the word exploit
                        line_found = line[num - 1:]  # grabs the line of the word exploit in
                        line_found = line_found.split()  # splits the sentence for each space
                        exploit_list.append(line_found[0])  # adds the first word to list
                        lstbox.insert(count, line_found[0])  # adds it to the listbox for the user to choose from
                        count = count + 1

        d = list()  # to store user input for options
        options_list = list()

        def run_exploit():
            open('/root/msf_output.txt', 'w').close()  # deletes previous log file created

            for i in range(len(d)):  # sets all of the options needed to run the exploit
                user_input = d[i]
                value = user_input.get()
                print(value)
                p1.stdin.write('set ' + options_list[i] + ' ' + value + '\n')
                p1.stdin.flush()
            p1.stdin.write('exploit\n')  # runs exploit
            p1.stdin.flush()

            time.sleep(15)
            with open('/root/msf_output.txt', "r") as lines:  # edits the output
                for line in lines:
                    if line.find("Exploit") > 0:  # prevents the next line being taken for the next iteration
                        num = int(line.find("Exploit"))  # searches for the index of the word exploit
                        line_found = line[num - 1:]  # grabs the line of the word exploit in
                    if line.find("] Command shell") > 0:  # prevents the next line being taken for the next iteration
                        num = int(line.find("Command"))  # searches for the index of the word exploit
                        line_found = line[num - 1:]  # grabs the line of the word exploit in
                        p1.stdin.write('pwd')
                        p1.stdin.flush()
            messagebox.showinfo("Message", line_found)

        txtLbl = tk.Label(inputframe, text="Platform/Protocol:")
        txtLbl.place(relx=0.23, rely=0.2)

        exploit_btn_packed = False

        def check_selected():
            global exploit_btn_packed  # to access a variable outside function
            self.after(200, check_selected)  # every 200ms rerun function
            L = lstbox.curselection()
            # text = str(exploit_list[L])
            try:  # try and except due to lstbox not having an index on start
                # txtLbl.config(text=lstbox.get(L[0]))
                # show targets
                if exploit_btn_packed == False and L[0] != None:  # makes sure that something has been selected
                    button = tk.Button(inputframe, text="Use Exploit", command=use_exploit)
                    button.place(relx=0.62, rely=0.2)
                    exploit_btn_packed = True
                return lstbox.get(L[0])  # so i can use the selected exploit

            except:
                exploit_btn_packed = False  # the allows the if statement to run again even if it failed
                pass
            # print(selection)

        def use_exploit():
            for widget in optionsframe.winfo_children():  # deletes everything in the previous input frame
                widget.destroy()

            outputframe.pack_forget()
            inputframe.pack_forget()

            optionsframe.pack(fill=BOTH, expand=FALSE)

            p1.stdin.write('use ' + check_selected() + '\n')
            p1.stdin.flush()
            open('/root/msf_output.txt', 'w').close()  # deletes previous log file created
            p1.stdin.write('show options\n')
            p1.stdin.flush()

            time.sleep(2)  # gives time to write to file
            #outputframe.pack()
            with open('/root/msf_output.txt',
                      "r") as lines:  # edits the output to find what needs to be inputted by the user for the exploit to run
                for line in lines:
                    if line.find("yes") > 0:
                        num = int(line.find("yes"))
                        line_found = line[:num + 3]
                        line_found = line_found.split()  # splits the sentence for each space
                        if line_found[1] == 'yes':
                            options_list.append(line_found[0])  # adds the first word to the list

            for i in range(len(options_list)): # this outputs what needs to be changed for the user
                # print("This needs to be changed: " + options_list[i]+'\n')
                tk.Label(optionsframe, text=options_list[i], fg='Black', font='bold').pack()
                d.append(Entry(
                    optionsframe))  # I had to store the tkinter entry widget in a list because it is in a loop and i need to reference each one
                entry = d[i]  # retrieving from list
                entry.pack()  # packing it to screen

            run_exploitbtn = tk.Button(optionsframe, text='Run exploit', command=run_exploit)
            run_exploitbtn.pack()

            def back():
                d.clear() #clears the previous lists
                options_list.clear()

                optionsframe.pack_forget()
                outputframe.pack(fill=BOTH, side=TOP, expand=TRUE)
                inputframe.pack(fill=BOTH, side=BOTTOM, expand=FALSE)

            backbtn = tk.Button(optionsframe, text='Back', command=back)
            backbtn.pack()

        check_selected()

        search_vuln_btn = tk.Button(inputframe, command=search_vulns, text='Search Exploits')
        search_vuln_btn.pack()


class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)  # pages are classes
        p2 = Page2(self)
        p3 = Page3(self)

        buttonframe = tk.Frame(self, bg=toolbarcolour)  # where buttons are kept
        container = tk.Frame(self)  # where pages are kept
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