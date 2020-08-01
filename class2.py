import tkinter as tk

root = tk.Tk()

root.geometry("800x650")
root.title("My Application")


def btn1_fun():
    fn = entry2.get()
    ln = entry3.get()
    email = entry4.get()
    pn = entry5.get()
    gn = v.get()
    coi = [str(c1), str(c2), str(c3)]

    with open("info.txt", "w") as file:
        file.write("'{}', '{}', '{}', '{}', '{}', '{}'".format(fn, ln, email, pn, gn, coi))

    print("finished!")


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

btn1 = tk.Button(root, text='Submit', font="Arial 14", command=btn1_fun)

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

btn1.grid(row=7, column=0, pady=(35, 0), columnspan=2)

root.mainloop()