import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import HelpPage


root = tk.Tk()

root.geometry("800x900")
root.title("My Application")


def clear_all_fields():
    all_entries = [entry2, entry3, entry4, entry5]
    all_chk = [c1, c2, c3]

    for entry in all_entries:
        entry.delete(0, "end")
    v.set("F")
    for chk in all_chk:
        chk.set(False)


def btn1_fun():
    all_labels = [label2, label3, label4, label5]
    for lbl in all_labels:
        lbl.config(fg='black')
    if entry2.get() == "" or entry3.get() == "":
        messagebox.askokcancel(title="Error Processing Form", message="You need to enter both first name and last name.")
        if entry2.get() == "":
            label2.config(fg='red')
        if entry3.get() == "":
            label3.config(fg='red')
    elif entry4.get() == "" and entry5.get() == "":
        messagebox.askokcancel(title="Error Processing Form",
                               message="You need to enter either an email or phone number for us to contact you.")
        label4.config(fg='red')
        label5.config(fg='red')
    else:
        fn = entry2.get()
        ln = entry3.get()
        email = entry4.get()
        pn = entry5.get()
        gn = v.get()
        coi = [str(c1.get()), str(c2.get()), str(c3.get())]

        with open("info.txt", "w") as file:
            file.write("'{}', '{}', '{}', '{}', '{}', '{}'".format(fn, ln, email, pn, gn, coi))

        messagebox.showinfo("Success", "Your information was saved successfully!")


def exit_():
    answer = messagebox.askyesno(title="Exit", message="Are you sure you want to exit?")
    if answer:
        root.quit()


def instantiate_help_window():
    HelpPage.Help()


menubar = tk.Menu(root)

filemenu = tk.Menu(menubar)

submenu = tk.Menu(filemenu)
submenu.add_command(label='Option 1')
submenu.add_command(label='Option 2')

filemenu.add_command(label="File")
filemenu.add_command(label="New", font="Arial 14", command=clear_all_fields)
filemenu.add_command(label="Open...")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exit_)

helpmenu = tk.Menu(menubar)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=instantiate_help_window)

root.config(menu=menubar)


txt = "Information Collection Form"

label1 = tk.Label(root, text=txt, font="Arial 18 bold")

label2 = tk.Label(root, text="First Name:", font="Arial 14")
entry2 = tk.Entry(root, width=40)

label3 = tk.Label(root, text="Last Name:", font="Arial 14")
entry3 = tk.Entry(root, width=40)

label4 = tk.Label(root, text="Email Address:", font="Arial 14")
entry4 = tk.Entry(root, width=40)

label5 = tk.Label(root, text="Phone Number:", font="Arial 14")
entry5 = tk.Entry(root, width=40)

frame1 = tk.Frame(root)
label6 = tk.Label(frame1, text="Gender:", font="Arial 14")

v = tk.StringVar()
v.set("F")
radio1 = tk.Radiobutton(frame1, text="Male", font="Arial 14", variable=v, value="M")
radio2 = tk.Radiobutton(frame1, text="Female", font="Arial 14", variable=v, value="F")

frame2 = tk.Frame(root)
label7 = tk.Label(frame2, text="Classes of Interest:", font="Arial 14")

c1 = tk.BooleanVar()
c2 = tk.BooleanVar()
c3 = tk.BooleanVar()
chk1 = tk.Checkbutton(frame2, text="Data Science", font="Arial 14", variable=c1)
chk2 = tk.Checkbutton(frame2, text="Application Development", font="Arial 14", variable=c2)
chk3 = tk.Checkbutton(frame2, text="Robotic Process Automation", font="Arial 14", variable=c3)

label8 = tk.Label(root, text="What kind of classroom setup are you interested in?", font="Arial 14")
combo1 = ttk.Combobox(root, font="Arial 14")
combo1['values'] = ("In Person", "Online Only", "Hybrid", "Don't care")
combo1.current(0)

label9 = tk.Label(root, text="How many people are interested in the class?", font="Arial 14")
spin1 = tk.Spinbox(root, from_=0, to=10, width=15, font="Arial 14")

label10 = tk.Label(root, text="If you have any special requests, enter below:", font="Arial 14")
text1 = tk.Text(root, width=45, height=5, font="Arial 14")

btn1 = tk.Button(root, text='Submit', font="Arial 14", command=btn1_fun)
btn2 = tk.Button(root, text='Reset', font="Arial 14", command=clear_all_fields)

################### GRIDDING ######################

label1.grid(row=0, columnspan=2, padx=(75, 0))

label2.grid(row=1, column=0, pady=(20, 0), padx=(60, 0), sticky='W')
label3.grid(row=1, column=1, pady=(20, 0), padx=(60, 0), sticky='W')

entry2.grid(row=2, column=0)
entry3.grid(row=2, column=1)

label4.grid(row=3, column=0, pady=(20, 0), padx=(60, 0), sticky='W')
label5.grid(row=3, column=1, pady=(20, 0), padx=(60, 0), sticky='W')

entry4.grid(row=4, column=0)
entry5.grid(row=4, column=1)

frame1.grid(row=5, column=0, pady=(35, 0), columnspan=2, padx=(50, 0))
label6.grid(row=0, column=0, columnspan=2)
radio1.grid(row=1, column=0, pady=(10, 0), padx=(50, 50))
radio2.grid(row=1, column=1, pady=(10, 0), padx=(50, 50))

frame2.grid(row=6, column=0, pady=(35, 0), columnspan=2, padx=(50, 0))
label7.grid(row=0, column=0, columnspan=3)
chk1.grid(row=1, column=0, pady=(15, 0), padx=(5, 5))
chk2.grid(row=1, column=1, pady=(15, 0), padx=(5, 5))
chk3.grid(row=1, column=2, pady=(15, 0), padx=(5, 5))

label8.grid(row=7, column=0, pady=(45, 0), columnspan=2)
combo1.grid(row=8, column=0, pady=(15, 0), columnspan=2)

label9.grid(row=9, column=0, pady=(45, 0), columnspan=2)
spin1.grid(row=10, column=0, pady=(15, 0), columnspan=2)

label10.grid(row=11, column=0, pady=(45, 0), columnspan=2)
text1.grid(row=12, column=0, columnspan=2)

btn1.grid(row=13, column=0, pady=(35, 0))
btn2.grid(row=13, column=1, pady=(35, 0))

root.mainloop()