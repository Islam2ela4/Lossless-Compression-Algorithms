from tkinter import *
from tkinter import messagebox

class RLE:

    #text_orignal = '111122233333311112222555'
    #text_binary = '1111110001110010000011111111'

    def __init__(self, window):
        self.window = window
        window.geometry('900x450+200+50')
        window.title('Shannon-Fano')
        window.configure(bg='gray')
        window.overrideredirect(1)

        self.main_label = Label(text='Run Length', fg='white', bg='gray',
                           font=("Times New Roman", 30, "bold"))
        self.main_label.pack(pady=30)

        self.text = Label(text='Text: ', fg='white', bg='gray', font=("Times New Roman", 18, "bold"))
        self.text.place(x=50, y=130)

        self.compression = Label(text='Compression : ', fg='white', bg='gray', font=("Times New Roman", 18, "bold"))
        self.compression.place(x=50, y=230)

        self.text_ = Entry(window, width=65, fg='black', bd='8', font=("Times New Roman", 15, "bold"))
        self.text_.place(x=200, y=130)

        self.compression_ = Entry(window, width=65, fg='black', bd='8', font=("Times New Roman", 15, "bold"))
        self.compression_.place(x=200, y=230)

        self.action1 = Button(text='Compress orignal', font=("Times New Roman", 14, "bold"), width=15, height=1, bg='green',
                            fg='white', bd=14, cursor='pirate', activebackground='red', activeforeground='black',
                            command=self.run_orignal)
        self.action1.place(x=550, y=320)

        self.action2 = Button(text='Compress binary', font=("Times New Roman", 14, "bold"), width=15, height=1, bg='red',
                              fg='white', bd=14, cursor='pirate', activebackground='green', activeforeground='black',
                              command=self.run_binary)
        self.action2.place(x=300, y=320)

        self.close = Button(text='X', font=("Times New Roman", 14, "bold"), width=3, height=1, bg='red', fg='white',
                       cursor='pirate', activebackground='green', activeforeground='black', command=self.close_)
        self.close.place(x=860, y=0)



    def RLE_orignal(self, input):
        input = input + '#'

        count = 1
        output = []
        for i in range(0, len(input)-1):
                    if input[i] == input[i+1]:
                        count += 1
                    elif input[i] != input[i+1]:
                        clause = (input[i], count)
                        output.append(clause)
                        count = 1

        return output


    def RLE_binary(self, input):
        input_ = input + '#'

        count = 1
        if input_[0] != '0':
            output = ['0']
        else:
            output = []

        for i in range(0, len(input_)-1):
            if input_[i] == input_[i+1]:
                count += 1
            elif input_[i] != input_[i+1]:
                output.append(count)
                count = 1

        return output



    def set_text(self, var, text):
        var.delete(0, END)
        var.insert(0, text)
        return



    def run_orignal(self):
        text = self.text_.get()
        if len(text) == 0:
            messagebox.showwarning('Warning...', 'Entry is empty !!!')
        else:
            com = self.RLE_orignal(text)
            self.set_text(self.compression_, com)


    def run_binary(self):
        text = self.text_.get()
        if len(text) == 0:
            messagebox.showwarning('Warning...', 'Entry is empty !!!')
        else:
            com = self.RLE_binary(text)
            self.set_text(self.compression_, com)


    def close_(self):
        self.window.destroy()


window = Tk()
gui = RLE(window)
window.mainloop()






