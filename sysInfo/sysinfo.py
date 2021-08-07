import tkinter as tk
from tkinter import FALSE, LEFT
import platform as pl

class sysInfo_MainClass:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title('sysInfo v1')
        self.window.configure(bg='black')
        self.window.geometry('600x500')
        self.window.resizable(FALSE,FALSE)

    def platform_data(self):

        system_label = tk.Label(self.window,text=f'OS: {pl.system()}',width=18, height=2, fg='#F0B90B', bg='black',
                                  font='Gotham 13 bold')

        arch_label = tk.Label(self.window, text=f'Arch: {pl.architecture()}', width=18, height=2, fg='#F0B90B', bg='black',
                                font='Gotham 13 bold')

        system_label.grid(ipadx=30, row=1)
        arch_label.grid(ipadx=30,row=2)



if __name__ == '__main__':
    sysInfo = sysInfo_MainClass()
    sysInfo.platform_data()
    sysInfo.window.mainloop()
