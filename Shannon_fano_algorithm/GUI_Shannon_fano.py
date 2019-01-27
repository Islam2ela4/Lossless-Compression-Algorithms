from tkinter import *
from tkinter import messagebox
from Shannon_fano_algorithm.Shannon_fano_structure import *

class GUI_Shannon_fano:

    shannon = Shannon_fano_structure()

    #text = 'acabadadeaabbaaaedcacdeaaabcdbbedcbacae'


    def __init__(self, window):
        self.window = window
        window.geometry('900x450+200+50')
        window.title('Shannon-Fano')
        window.configure(bg='#2F4F4F')
        window.overrideredirect(1)

        self.main_label = Label(text='Shannon-Fano', fg='white', bg='#2F4F4F',
                           font=("Times New Roman", 30, "bold"))
        self.main_label.pack(pady=30)

        self.text = Label(text='Text: ', fg='white', bg='#2F4F4F', font=("Times New Roman", 18, "bold"))
        self.text.place(x=50, y=130)

        self.dictionary = Label(text='Dictionary : ', fg='white', bg='#2F4F4F', font=("Times New Roman", 18, "bold"))
        self.dictionary.place(x=50, y=200)

        self.compression = Label(text='Compression : ', fg='white', bg='#2F4F4F', font=("Times New Roman", 18, "bold"))
        self.compression.place(x=50, y=270)

        self.text_ = Entry(window, width=65, fg='black', bd='8', font=("Times New Roman", 15, "bold"))
        self.text_.place(x=200, y=130)

        self.dictionary_ = Entry(window, width=65, fg='black', bd='8', font=("Times New Roman", 15, "bold"))
        self.dictionary_.place(x=200, y=200)

        self.compression_ = Entry(window, width=65, fg='black', bd='8', font=("Times New Roman", 15, "bold"))
        self.compression_.place(x=200, y=270)

        self.action = Button(text='Compress', font=("Times New Roman", 14, "bold"), width=15, height=1, bg='#2E8B57',
                            fg='white', bd=14, cursor='pirate', activebackground='#90EE90', activeforeground='black',
                            command=self.compress_)
        self.action.place(x=400, y=350)

        self.close = Button(text='X', font=("Times New Roman", 14, "bold"), width=3, height=1, bg='red', fg='white',
                       cursor='pirate', activebackground='green', activeforeground='black', command=self.close_)
        self.close.place(x=860, y=0)



    def set_text(self, var, text):
        var.delete(0, END)
        var.insert(0, text)
        return



    def compress_(self):
        text = self.text_.get()
        if len(text) == 0:
            messagebox.showwarning('Warning...', 'Entry is empty !!!')
        else:
            x = self.shannon.create_list(text)
            m = self.shannon.shannon_fano_structure(x)
            self.set_text(self.dictionary_, m)
            com = self.shannon.compression(text)
            self.set_text(self.compression_, com)



    def close_(self):
        self.window.destroy()


window = Tk()
gui = GUI_Shannon_fano(window)
window.mainloop()

