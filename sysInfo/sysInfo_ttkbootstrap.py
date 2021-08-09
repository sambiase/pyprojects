from ttkbootstrap import Style
from tkinter import ttk

style = Style(theme='superhero')
window = style.master
window.geometry('400x300')

label_frame = ttk.LabelFrame(window,text='sysInfo')
sys_label = ttk.Label(label_frame,text='Teste',font = ' Calibri 18 bold',width=30)
exit_btn = ttk.Button(label_frame,text='Exit', style='success.Outline.TButton')
comboBox = ttk.Combobox(label_frame)

label_frame.pack()
sys_label.pack(padx=30)
comboBox.pack()
exit_btn.pack()
window.mainloop()
