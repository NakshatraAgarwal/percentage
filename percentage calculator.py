from tkinter import *
root = Tk()

root.geometry("1000x1000")
root.title("Percentage")



g8 = Label(root)
g10 = Label(root)
g12 = Label(root)



class Grade8():
    def __init__(self, English, Maths, Science, SST, nd2_Language, rd3_Language):
        self.eng = English
        self.math = Maths
        self.sci = Science
        self.sst = SST
        self.l2 = nd2_Language
        self.l3 = rd3_Language
    def percentage(self):
        total = self.eng + self.math + self.sci + self.sst + self.l2 + self.l3
        g8p = total / 6
        g8["text"] = str(g8p) + "%" 
        
    
class Grade10():
    def __init__(self, English, Maths, Science, SST, nd2_Language):
        self.eng = English
        self.math = Maths
        self.sci = Science
        self.sst = SST
        self.l2 = nd2_Language
        
    def percentage(self):
        total = self.eng + self.math + self.sci + self.sst + self.l2
        g10p = total / 5
        g10["text"] = str(g10p) + "%"
        

class Grade12():
    def __init__(self, English, Maths, Physics, Chemistry, Computer_Science):
        self.eng = English
        self.math = Maths
        self.phy = Physics
        self.chem = Chemistry
        self.cs = Computer_Science
        
    def percentage(self):
        total = self.eng + self.math + self.phy + self.chem + self.cs
        g12p = total / 5
        g12["text"] = str(g12p) + "%" 

        

grade8 = Grade8(87, 100, 97, 90, 95, 80)
btn_g8 = Button(root, text =  "Grade 8 Percentage", command = grade8.percentage)
btn_g8.pack()
g8.pack(padx = 20, pady = 10)

grade10 = Grade10(96, 100, 99, 97, 98)
btn_g10 = Button(root, text = "Grade 10 Percentage", command = grade10.percentage)
btn_g10.pack()
g10.pack(padx = 20, pady = 10)

grade12 = Grade12(98, 100, 99, 99, 100)
btn_g12 = Button(root, text = "Grade 12 Percentage", command = grade12.percentage)
btn_g12.pack()
g12.pack(padx = 20, pady = 10)

root.mainloop()
    