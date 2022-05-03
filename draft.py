import tkinter as tk
from tkinter.font import NORMAL
import tkinter.messagebox
import mysql
import write

class Draft:
    def __init__(self, sen):
        self.win = tk.Tk()
        self.num = tk.Text(self.win, height=1, width=25)
        self.lis = []
        self.sql = mysql.Mysql()
        self.__send = sen

    def check(self):
        index = int(self.num.get('1.0', tk.END))        
        msg = self.lis[index - 1]
        wri = write.Write(self.__send)
        wri.openAsDraft(msg[1], msg[2], msg[3], msg[4])
        
    def window(self):
        self.win.title('草稿箱')
        self.win.geometry('500x300')
        self.lis = self.sql.searchList()
        text = tk.Text(self.win, height=15, width=62)
        text.place(x=30, y=30)
        for i in self.lis:
            for j in range (len(i)):
                if j == 1:
                    continue
                text.insert(tkinter.INSERT, i[j])

        tk.Label(self.win, text='邮件编号：').place(x = 50, y=250)
        self.num.place(x = 130, y = 250)
        tk.Button(self.win, text='查看', command=self.check).place(x = 300, y = 250)
        self.win.mainloop()
