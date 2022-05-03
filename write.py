import hashlib
import tkinter as tk
import send
import mysql
import re
class Write:
    def __init__(self, sen):
        self.__send = sen
        self.win = tk.Tk()
        self.title = tk.Text(self.win, height=1, width=30)
        self.to = tk.Text(self.win, height=1, width=30)
        self.text = tk.Text(self.win, height=12, width=54)
        self.id = 0

    def send(self):
        title = self.title.get('1.0', tk.END)
        to = self.to.get('1.0', tk.END)
        text = self.text.get('1.0', tk.END)
        to = to.strip()
        title = title.strip()
        text = text.strip()
        regex = '^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}$' 
        if re.match(regex, to):
            pass
        else:
            tk.messagebox.showinfo('提示', '邮箱格式不正确', parent = self.win)
            return

        if self.__send.send_mail(title, to, text):
            tk.messagebox.showinfo('提示', '发送成功', parent = self.win)
        else:
            tk.messagebox.showinfo('提示', '发送失败', parent = self.win)


    def save(self):
        sql = mysql.Mysql()
        title = self.title.get('1.0', tk.END)
        to = self.to.get('1.0', tk.END)
        text = self.text.get('1.0', tk.END)
        to = to.strip()
        title = title.strip()
        text = text.strip()
        
        regex = '^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}$' 
        if re.match(regex, to):
            pass
        else:
            tk.messagebox.showinfo('提示', '邮箱格式不正确', parent = self.win)
            return

        if sql.search(self.id):
            if sql.upd(self.id, title, to, text):
                tk.messagebox.showinfo('提示', '保存成功', parent = self.win)
            else:
                tk.messagebox.showinfo('提示', '保存失败', parent = self.win)

        elif sql.insert(title, to, text):
            tk.messagebox.showinfo('提示', '保存成功', parent = self.win)
        else:
            tk.messagebox.showinfo('提示', '保存失败', parent = self.win)

    def openAsDraft(self, id, title, to, text):
        self.id = id
        self.title.insert(tk.INSERT, title)
        self.to.insert(tk.INSERT, to)
        self.text.insert(tk.INSERT, text)
        self.window()


    def window(self):
        self.win.title('写信')
        self.win.geometry('500x300')
        tk.Label(self.win, text='收件人').place(x=20, y=20)
        self.to.place(x=70, y=20)
        tk.Label(self.win, text='主题   ').place(x=20, y=50)
        self.title.place(x=70, y=50)
        tk.Label(self.win, text='正文   ').place(x=20, y=80)
        self.text.place(x=70, y=80)
        tk.Button(self.win, text='保存草稿', command=self.save).place(x = 130, y = 250)
        tk.Button(self.win, text='发送', command=self.send).place(x = 200, y = 250)