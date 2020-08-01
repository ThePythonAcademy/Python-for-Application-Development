import tkinter as tk


class Help():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x300")
        self.root.title("Help Window")
        self.root.mainloop()


class BBB(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Help Window")
        self.geometry("500x300")
        tk.Label(self, text="Hello world!").pack()


if __name__ == "__main__":
    root = BBB()
    root.mainloop()


class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def say_names(self):
        print("Hi, my name is", self.first_name, self.last_name)

    def say_age(self):
        print("My age is", self.age)


class Student(Person):
    def __init__(self, first_name, last_name, age, discount):
        super().__init__(first_name, last_name, age)
        self.discount = discount


