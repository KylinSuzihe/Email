from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
 
class Send:
    def __init__(self, from_addr, password, server, port):
        self.from_addr = from_addr
        self.password = password
        self.server = server
        self.port = port


    def _format_addr(self, s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))
    
    
    def send_mail(self, sub, to_addr, text):
        msg = MIMEMultipart()
        msg['From'] = self._format_addr('发送者 <%s>' % self.from_addr)
        msg['To'] = self._format_addr('接受者 <%s>' % to_addr)
        msg['Subject'] = Header(sub, 'utf-8').encode()
    
        txt = MIMEText(text, _subtype='plain', _charset='utf8')
        msg.attach(txt)
 
        try:
            server = smtplib.SMTP_SSL(self.server, self.port)
            server.login(self.from_addr, self.password)
            # 发邮件
            server.sendmail(self.from_addr, to_addr, msg.as_string())
            server.quit()
            return True
        except:
            print("出现错误！")
            return False
    
    def logIn(self):
        try:
            server = smtplib.SMTP_SSL(self.server, self.port)
            server.login(self.from_addr, self.password)
            return True
        except:
            return False
        