import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import HelpPage
import sqlite3


conn = sqlite3.connect('database.db')
cur = conn.cursor()

root = tk.Tk()

screen_height = root.winfo_screenheight()
screen_width = root.winfo_screenwidth()

root_height = int(0.88 * screen_height)
root_width = int(0.5 * screen_width)

geo = "{}x{}".format(root_width, root_height)
print(geo)

root.geometry(geo)
root.title("My Application")

# root.resizable(0, 0)
root.columnconfigure((0, 1), weight=1)
root.rowconfigure((2, 3), weight=1)

root.option_add("*Font", "Arial 14")
root.option_add("*background", "white")
root.configure(bg='white')


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

        try:
            querry = "INSERT INTO 'ApplicationForms' (FirstName, LastName, PhoneNumber, EmailAddress, GenderIdentifier) VALUES (?,?,?,?,?)"

            cur.execute(querry, (fn, ln, pn, email, gn))
            conn.commit()

            messagebox.showinfo("Success", "Your information was saved successfully!")

        except:
            messagebox.showwarning("Error", "Sorry, we could not save your info into our database. Please contact us.")


def exit_():
    answer = messagebox.askyesno(title="Exit", message="Are you sure you want to exit?")
    if answer:
        root.quit()


def instantiate_help_window():
    HelpPage.Help()


menubar = tk.Menu(root)

file_menu = tk.Menu(menubar)

new_submenu = tk.Menu(file_menu)
new_submenu.add_command(label="Option 1")
new_submenu.add_command(label="Option 2")

menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_cascade(label="New", menu=new_submenu)
file_menu.add_command(label="Exit", command=exit_)

help_menu = tk.Menu(menubar)
menubar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label='About Us', command=instantiate_help_window)

root.config(menu=menubar)


img1 = tk.PhotoImage(file=r"C:\Users\15405\Desktop\Python Academy\Logo\small-2.png")

img_label = tk.Label(image=img1)

txt = "Information Collection Form"

label1 = tk.Label(root, text=txt, font="Arial 18 bold")

label2 = tk.Label(root, text="First Name:")
entry2 = tk.Entry(root, width=40, font="Arial 10")

label3 = tk.Label(root, text="Last Name:")
entry3 = tk.Entry(root, width=40, font="Arial 10")

label4 = tk.Label(root, text="Email Address:")
entry4 = tk.Entry(root, width=40, font="Arial 10")

label5 = tk.Label(root, text="Phone Number:")
entry5 = tk.Entry(root, width=40, font="Arial 10")

frame1 = tk.Frame(root)
label6 = tk.Label(frame1, text="Gender:")

v = tk.StringVar()
v.set("F")
radio1 = tk.Radiobutton(frame1, text="Male", variable=v, value="M")
radio2 = tk.Radiobutton(frame1, text="Female", variable=v, value="F")

frame2 = tk.Frame(root)
label7 = tk.Label(frame2, text="Classes of Interest:")

c1 = tk.BooleanVar()
c2 = tk.BooleanVar()
c3 = tk.BooleanVar()
chk1 = tk.Checkbutton(frame2, text="Data Science", variable=c1)
chk2 = tk.Checkbutton(frame2, text="Application Development", variable=c2)
chk3 = tk.Checkbutton(frame2, text="Robotic Process Automation", variable=c3)

label8 = tk.Label(root, text="What kind of classroom setup are you interested in?")
combo1 = ttk.Combobox(root, font="Arial 14")
combo1['values'] = ("In Person", "Online Only", "Hybrid", "Don't care")
combo1.current(0)

label9 = tk.Label(root, text="How many people are interested in the class?")
spin1 = tk.Spinbox(root, from_=0, to=10, width=15)

label10 = tk.Label(root, text="If you have any special requests, enter below:")
text1 = tk.Text(root, width=45, height=5)

btn1 = tk.Button(root, text='Submit', command=btn1_fun)
btn2 = tk.Button(root, text='Reset', command=clear_all_fields)

################### GRIDDING ######################


rel_padding = 0.1 * root_width

img_label.grid(row=0, columnspan=2)
label1.grid(row=1, columnspan=2)

label2.grid(row=2, column=0, pady=(20, 0), sticky="W", padx=(rel_padding, 0))
label3.grid(row=2, column=1, pady=(20, 0), sticky="W", padx=(rel_padding, 0))

entry2.grid(row=3, column=0, sticky="W", padx=(rel_padding, 0))
entry3.grid(row=3, column=1, sticky="W", padx=(rel_padding, 0))

label4.grid(row=4, column=0, pady=(20, 0), sticky="W", padx=(rel_padding, 0))
label5.grid(row=4, column=1, pady=(20, 0), sticky="W", padx=(rel_padding, 0))

entry4.grid(row=5, column=0, sticky="W", padx=(rel_padding, 0))
entry5.grid(row=5, column=1, sticky="W", padx=(rel_padding, 0))

frame1.grid(row=6, column=0, pady=(35, 0), columnspan=2, padx=(50, 0))
label6.grid(row=0, column=0, columnspan=2)
radio1.grid(row=1, column=0, pady=(10, 0), padx=(50, 50))
radio2.grid(row=1, column=1, pady=(10, 0), padx=(50, 50))

frame2.grid(row=7, column=0, pady=(35, 0), columnspan=2, padx=(50, 0))
label7.grid(row=0, column=0, columnspan=3)
chk1.grid(row=1, column=0, pady=(15, 0), padx=(5, 5))
chk2.grid(row=1, column=1, pady=(15, 0), padx=(5, 5))
chk3.grid(row=1, column=2, pady=(15, 0), padx=(5, 5))

label8.grid(row=8, column=0, pady=(45, 0), columnspan=2)
combo1.grid(row=9, column=0, pady=(15, 0), columnspan=2)

label9.grid(row=10, column=0, pady=(45, 0), columnspan=2)
spin1.grid(row=11, column=0, pady=(15, 0), columnspan=2)

label10.grid(row=12, column=0, pady=(45, 0), columnspan=2)
text1.grid(row=13, column=0, columnspan=2)

btn1.grid(row=14, column=0, pady=(35, 0))
btn2.grid(row=14, column=1, pady=(35, 0))

root.mainloop()