import tkinter as tk
from tkinter import FALSE, LEFT, TOP, RIGHT
import platform as pl


class sysInfo_MainClass:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title('sysInfo v1')
        self.window.configure(bg='black')
        self.window.geometry('350x400')
        self.window.resizable(FALSE,FALSE)


    def platform_data(self):

        system_label_frame = tk.Frame(self.window)
        cpu_label_frame = tk.Frame(self.window)
        arch_label_frame = tk.Frame(self.window)

        system_label = tk.Label(system_label_frame,text='OS',width=18, height=2, fg='#F0B90B', bg='black',
                                  font='Calibri 18 bold')
        system_label_res = tk.Label(system_label_frame,text=f'{pl.system()}',width=18, height=2, fg='#F0B90B', bg='black',
                                  font='Calibri 18 bold')

        cpu_label = tk.Label(cpu_label_frame, text=f'CPU: {pl.processor()}', width=18, height=2, fg='#F0B90B', bg='black',
                                font='Gotham 13 bold')

        arch_label = tk.Label(arch_label_frame, text=f'Arch: {pl.architecture()}', width=18, height=2, fg='#F0B90B', bg='black',
                                font='Gotham 13 bold')


        system_label_frame.pack(side=TOP,pady=50)
        system_label.pack(side=LEFT)
        system_label_res.pack(side=RIGHT)

        cpu_label_frame.pack(side=TOP)
        cpu_label.pack(side=LEFT)

        arch_label_frame.pack(side=TOP)
        arch_label.pack(side=LEFT)







if __name__ == '__main__':
    sysInfo = sysInfo_MainClass()
    sysInfo.platform_data()
    sysInfo.window.mainloop()
