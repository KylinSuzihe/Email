import tkinter as tk
from tkinter.font import NORMAL
import tkinter.messagebox
import accept

class Inbox:
    def __init__(self, user, pwd, host):
        self.user = user
        self.pwd = pwd
        self.host = host
        self.win = tk.Tk()
        self.num = tk.Text(self.win, height=1, width=25)
        self.acc = accept.Accept(self.user, self.pwd, self.host)

    def check(self):
        win = tk.Toplevel(self.win)
        win.title('邮件')
        win.geometry('500x300')
        index = self.num.get('1.0', tk.END)
        msg = self.acc.print_info(index).split(':')
        
        tk.Label(win, text='Title       : ' + msg[1]).place(x = 30, y=30)
        tk.Label(win, text='From     : ' + msg[0]).place(x = 30, y=50)
        tk.Label(win, text='Content : ' + msg[2]).place(x = 30, y=70)
        win.mainloop()
        
    def window(self):
        self.win.title('收件箱')
        self.win.geometry('500x300')
        self.acc.connect()
        lis = self.acc.getMailList()
        text = tk.Text(self.win, height=15, width=62)
        text.place(x=30, y=30)
        for i in lis:
            text.insert(tkinter.INSERT, i)

        tk.Label(self.win, text='邮件编号：').place(x = 50, y=250)
        self.num.place(x = 130, y = 250)
        tk.Button(self.win, text='查看', command=self.check).place(x = 300, y = 250)
        self.win.mainloop()
