import tkinter as tk
from typing import Text, final



default_font = ('Arial',20)
gray ='#F5F5F5'
lablec ='#25265E'
smal_font =('Arial',16)
larg_font =('Arial',40,'bold')

class calculator:

    def __init__(self):
        self.window =tk.Tk()
        #self.icon = tk.PhotoImage(file= 'C:\\Users\\mazin\\OneDrive\\Desktop\\icon.png')
        #self.window.iconphoto(True,self.icon) you can idite bath to change program icon
        self.window.geometry("375x667")
        self.window.resizable(0,0)
        self.window.title("calculator")
        self.dis_frame = self.create_dis_frame()
        self.button_frame = self.create_button_frame()
        self.total =''
        self.current =''
        self.lab ,self.total_lable = self.create_lable()
        self.digits = {
            7:(1,1),8:(1,2),9:(1,3),
            4:(2,1),5:(2,2),6:(2,3),
            1:(3,1),2:(3,2),3:(3,3),
            '.':(4,1),0:(4,2)
            }
        self.digit_button()
        self.op = { '/':"\u00F7",'*':"\u00D7",'-':'-','+':'+'}
        self.op_button()
        self.special_button()
        self.button_frame.rowconfigure(0, weight =1)
        for i in range(1,5):
            self.button_frame.rowconfigure(i, weight =1)
            self.button_frame.columnconfigure(i, weight =1)
        self.bind()





    def bind(self):
        self.window.bind('<Return>',lambda event :self.evaluate())
        for key in self.digits:
            self.window.bind(str(key),lambda event,digit =key : self.add_to_lable(digit))
        for key in self.op:
            self.window.bind(key,lambda event, operator = key: self.add_operator_to_lable(operator))
    def special_button(self):
        self.equal_button()
        self.clear_button()


    def add_to_lable(self, value):
        self.current += str(value)
        self.update_lable()


    def add_operator_to_lable(self,operator):
            self.current += operator
            self.total += self.current
            self.current =""
            self.update_total_lable()
            self.update_lable


    def create_lable(self):
        total_lable = tk.Label(self.dis_frame,text= self.total,bg =gray,anchor= tk.E,
                               fg =lablec,font=smal_font,padx =24)
        total_lable.pack(expand= True, fill ='both')

        lab = tk.Label(self.dis_frame,text= self.current,bg =gray,
                               fg =lablec,font=larg_font,padx=24,anchor= tk.E)
        lab.pack(expand= True, fill ='both')
        return lab,total_lable
    def op_button(self):
        i =0
        for operator,sympol in self.op.items():
            button = tk.Button(self.button_frame,bg='#FFFFFF', font= default_font,
                              borderwidth= 0,text = sympol,
                             command= lambda s = operator: self.add_operator_to_lable(s))
            button.grid(row = i, column = 4 ,sticky = tk.NSEW)
            i += 1

    def clear(self):
        self.current = ""
        self.total = ""
        self.update_lable()
        self.update_total_lable()

    def evaluate(self):
        self.total += self.current
        self.update_total_lable()
        try:
            self.current =str(eval(self.total))

            self.total = ""
        except Exception as e :
            self.current = 'error'
        finally:
            self.update_lable()

    def digit_button(self):
        
        for digit,gridV in self.digits.items():
            buttom = tk.Button(self.button_frame,text = digit ,bg='#FFFFFF',fg=lablec,
                               font=('Arial',24,'bold'),borderwidth =0,
                              command = lambda x= digit : self.add_to_lable(x)   )
            buttom.grid(row = gridV[0],column = gridV[1], sticky= tk.NSEW)

    def clear_button(self):
        button =tk.Button(self.button_frame,text ='C',bg = "#FFFFFF",fg = lablec,
                          font= default_font,borderwidth =0, command = self.clear )
        button.grid(row =0, column=1, columnspan =3, sticky= tk.NSEW )

    


    def equal_button(self):
        button =tk.Button(self.button_frame,text ='=',bg = "#CCEDFF",fg = lablec,
                          font= default_font,borderwidth =0,command = self.evaluate)
        button.grid(row =4, column=3, columnspan =2, sticky= tk.NSEW )



    def create_dis_frame(self):
        frame = tk.Frame(self.window,height =221 ,bg =gray)
        frame.pack(expand = True, fill ='both')
        return frame

    def update_total_lable(self):
        exp = self.total
        for operator,symbol in self.op.items():
            exp = exp.replace(operator,f'{symbol}')

        self.total_lable.config(text= exp )

    def update_lable(self):
        self.lab.config(text= self.current[:11] )


    def create_button_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand = True, fill ='both')
        return frame

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calc = calculator()
    calc.run()  
