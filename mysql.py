from unittest import result
import pymysql

class Mysql:
    def __init__(self):
        self.conn = pymysql.connect(host='', port=3306, user='', passwd='', database='')
        self.cursor = self.conn.cursor()

    def insert(self, title, to, text):
        try:
            self.cursor.execute('insert into draft(title, to_addr, text)\
                values("%s", "%s", "%s")' % (title, to, text))
            self.conn.commit()
            return True
        except:
            return False
    
    def searchList(self):
        self.cursor.execute('select id, title, to_addr, text from draft')
        li = self.cursor.fetchall()
        ans = []
        j = 0
        for i in li:
            j = j + 1
            s = []
            s.append(j)
            s.append(i[0])
            s.append(i[1] + '\n')
            s.append(i[2] + '\n')
            s.append(i[3] + '\n')
            ans.append(s)
        return ans

    def search(self, id):
        row = self.cursor.execute('select * from draft where id = %s' % id)
        return row == 1

    def upd(self, id, title, to, text):
        try:
            self.cursor.execute('update draft set title = "%s", to_addr = "%s", text = "%s" where id = %s' % (title, to, text, id))
            return True
        except:
            return False

