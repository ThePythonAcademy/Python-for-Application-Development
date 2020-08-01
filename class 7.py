import tkinter as tk
from tkinter import ttk
import logging


class SimpleApp(tk.Tk):
    def __init__(self):
        super().__init__()

        log_format = "%(levelname)s %(asctime)s - %(message)s"
        logging.basicConfig(filename="second_app.log", level=logging.DEBUG, format=log_format)
        self.logger = logging.getLogger()

        self.logger.info("Session Start")

        style = ttk.Style()
        style.theme_use("vista")
        style.configure("TButton", foreground="green", background="blue")
        style.configure("theme1.TButton", foreground="red", background="blue")
        style.configure(".", font="Arial 12")

        ttk.Label(self, text="Hello, welcome to our app. Please log in to proceed.", font = "Arial 16 bold").pack(pady=(5, 0))
        ttk.Label(self, text="Username:").pack(pady=(15, 0))
        entry1 = ttk.Entry(self)
        entry1.pack()
        entry1.bind("<Button-1>", self.entry_click)
        ttk.Label(self, text="Password:").pack(pady=(15, 0))
        ttk.Entry(self).pack()
        remember = tk.BooleanVar()
        ttk.Checkbutton(self, text='Remember Me', variable=remember, command=self.check_clicked).pack(pady=(15, 0))
        ttk.Button(self, text="Log In").pack(pady=(15, 0))
        ttk.Button(self, text="Exit", command=self.quit_application, style="theme1.TButton").pack(pady=(15, 15))

    def quit_application(self):
        self.logger.info("Session End")
        self.quit()

    def check_clicked(self):
        self.logger.info("Checkbox Click")

    def entry_click(self, event):
        self.logger.debug("Clicked on entry")


if __name__ == "__main__":
    root = SimpleApp()
    root.mainloop()