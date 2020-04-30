from tkinter import *
class Calculator(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.pack(expand=YES, fill=BOTH)
        self.master.title('计算器')
        self.master.rowconfigure( 0, weight = 1 )
        self.master.columnconfigure( 0, weight = 1 )
        self.grid( sticky = W+E+N+S )
        display = StringVar()
        entry = Entry(self, relief=SUNKEN, textvariable=display)
        entry.grid(row=0, column=0, columnspan=4, sticky=W+E+N+S)
        grid = '789+456-123*0./='
        for index,textChar in enumerate(grid):
            a = Button(self, text=textChar, width=5, command=lambda text=textChar:display.set(display.get() + text))
            a.grid(row=1+index//4, column=index%4)
            button_text = a.cget("text")
            if button_text == '=':
                a.config(command=lambda:display.set(eval(display.get())))
            b = Button(self, text="clear", width=20, command=lambda:display.set(""))
            b.grid(row=7, column=0, columnspan=4, sticky=W+E+N+S)
if __name__ == '__main__':
    Calculator().mainloop()