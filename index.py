import tkinter as tk
import tkinter.messagebox 
import accept
import send
import inbox
import write
import draft

class Index:
    def __init__(self):
        self.win = tk.Tk()
        self.userName = tk.Variable()
        self.password = tk.Variable()
        self.server = tk.Variable()
        self.port = tk.Variable()
        self.b = 0
        self.sen = None
    
    def logIn(self):
        self.sen = send.Send(self.userName.get(), self.password.get(), self.server.get(), self.port.get())
        if self.sen.logIn():
            self.b = 1
            tk.messagebox.showinfo('提示', '登陆成功！', parent = self.win)
        else:
            tk.messagebox.showinfo('提示', '登陆失败！', parent = self.win)
        
        
    def toinbox(self):
        if self.b == 0:
            tk.messagebox.showwarning('提示', '请先登录', parant = self.win)
            return
        inb = inbox.Inbox(self.userName.get(), self.password.get(), self.server.get())
        inb.window()

    def towrite(self):
        if self.b == 0:
            tk.messagebox.showwarning('提示', '请先登录', parant = self.win)
            return
        wri = write.Write(self.sen)
        wri.window()

    def todraft(self):
        if self.b == 0:
            tk.messagebox.showwarning('提示', '请先登录', parant = self.win)
            return
        dra = draft.Draft(self.sen)
        dra.window()

    def window(self):
        self.win.title('邮箱')
        self.win.geometry('500x300')
        frameLeft = tk.Frame(self.win, height=300, width=150)
        frameRight = tk.Frame(self.win, height=300, width=350)
        frameLeft.place(x=0, y=0)
        frameRight.place(x=150, y=0)

        tk.Button(frameLeft, text='收件箱', command=self.toinbox).place(x=70, y=60)
        tk.Button(frameLeft, text='写   信', command=self.towrite).place(x=70, y=120)
        tk.Button(frameLeft, text='草稿箱', command=self.todraft).place(x=70, y=180)
        
        tk.Label(frameRight, text="用户名：").place(x=60, y=50)
        tk.Entry(frameRight, textvariable=self.userName).place(x=120, y=50)
        tk.Label(frameRight, text="密   码：").place(x=60, y=110)
        tk.Entry(frameRight, textvariable=self.password, show='*').place(x=120, y=110)
        tk.Label(frameRight, text="服务器：").place(x=60, y=170)
        tk.Entry(frameRight, textvariable=self.server).place(x=120, y=170)
        tk.Label(frameRight, text="端   口：").place(x=60, y=230)
        tk.Entry(frameRight, textvariable=self.port).place(x=120, y=230) 
        
        tk.Button(frameRight, text='登录', command=self.logIn).place(x=150, y=250)

        self.win.mainloop()
index = Index()
index.window()
