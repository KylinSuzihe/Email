import poplib
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

class Accept:
    def __init__(self, user, pwd, host):
        self.user = user
        self.pwd = pwd
        self.host = host
        self.mailList = []
        pass

    def connect(self):
        server = poplib.POP3(self.host)
        server.user(self.user)
        server.pass_(self.pwd)
        resp, mails, octets = server.list()
        index = len(mails)
        for i in range (index) :
            i = i + 1
            resp, lines, octets = server.retr(i)
            msg_content = b'\r\n'.join(lines).decode('utf-8')
            msg = Parser().parsestr(msg_content)
            self.mailList.append(msg)

    def getMailList(self):
        headList = []
        j = 0
        for i in self.mailList:
            j = j + 1
            s = '' + str(j) + ': '
            for header in ['From', 'Subject']: 
                value = i.get(header, '')
                if value:
                    if header == 'Subject':
                        value = self.decode_str(value) 
                    else:                        
                        hdr, addr = parseaddr(value)  
                        name = self.decode_str(hdr)  
                        value = U'%s <%s>' % (name, addr) 
                s += header + ': ' + value + '\n   '
            headList.append(s)
        return headList

    def print_info(self, index):
        index = int(index)
        index = index - 1
        s = ''
        msg = self.mailList[index]
        for header in ['From', 'Subject']: 
            value = msg.get(header, '')
            if value:
                if header == 'Subject':
                    value = self.decode_str(value)  
                else:                        
                    hdr, addr = parseaddr(value) 
                    name = self.decode_str(hdr) 
                    value = U'%s <%s>' % (name, addr) 
            s += value + ':'

        msg = msg.get_payload()[0]
        content_type = msg.get_content_type()
        if content_type == 'text/plain' or content_type == 'text/html':
            content = msg.get_payload(decode=True)
            charset = self.guess_charset(msg)
            if charset:
                content = content.decode(charset)
            s += content
        else:
            print('Attachment: %s' % (content_type))
        return s

    def decode_str(self, s):
        value, charset = decode_header(s)[0] 
        if charset:
            value = value.decode(charset)
        return value

    def guess_charset(self, msg):
        charset = msg.get_charset()
        if charset is None:
            content_type = msg.get('Content-Type', '').lower()
            pos = content_type.find('charset=')
            if pos >= 0:
                charset = content_type[pos + 8:].strip()
        return charset
