from tkinter import *
from tkinter import messagebox
from Huffman_algorithm.Huffman_structure import *

class GUI_Huffman:

    huffman = Huffman_structure()

    #text = ''bbbbbbbdddddaas''


    def __init__(self, window):
        self.window = window
        window.geometry('900x450+200+50')
        window.title('Shannon-Fano')
        window.configure(bg='#B22222')
        window.overrideredirect(1)

        self.main_label = Label(text='Huffman', fg='white', bg='#B22222',
                           font=("Times New Roman", 30, "bold"))
        self.main_label.pack(pady=30)

        self.text = Label(text='Text: ', fg='white', bg='#B22222', font=("Times New Roman", 18, "bold"))
        self.text.place(x=50, y=130)

        self.dictionary = Label(text='Dictionary : ', fg='white', bg='#B22222', font=("Times New Roman", 18, "bold"))
        self.dictionary.place(x=50, y=200)

        self.compression = Label(text='Compression : ', fg='white', bg='#B22222', font=("Times New Roman", 18, "bold"))
        self.compression.place(x=50, y=270)

        self.text_ = Entry(window, width=65, fg='black', bd='8', font=("Times New Roman", 15, "bold"))
        self.text_.place(x=200, y=130)

        self.dictionary_ = Entry(window, width=65, fg='black', bd='8', font=("Times New Roman", 15, "bold"))
        self.dictionary_.place(x=200, y=200)

        self.compression_ = Entry(window, width=65, fg='black', bd='8', font=("Times New Roman", 15, "bold"))
        self.compression_.place(x=200, y=270)

        self.action = Button(text='Compress', font=("Times New Roman", 14, "bold"), width=15, height=1, bg='#8B0000',
                            fg='white', bd=14, cursor='pirate', activebackground='#CD5C5C', activeforeground='black',
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
            x = self.huffman.huffman(text)
            self.set_text(self.dictionary_, x)

            com = self.huffman.compression(text)
            self.set_text(self.compression_, com)



    def close_(self):
        self.window.destroy()


window = Tk()
gui = GUI_Huffman(window)
window.mainloop()

