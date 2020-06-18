#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/18
# @Author  : lin
# @FileName: AODI.py

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
import requests
import time
import json
import re

# e-mail config
SMTP_server = "" # mail server
password = "" # mail login password
sender = "" # mail send acount
receiver = "" # mail recieve account
subject = "[RPI]IP INFORM (FROM STMP)"
content = "Your Public IP is : "

# public IP config
headers = {
    "DNT": "1",
    "User-Agent": "User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"
}
url_source = ["http://ipv4.icanhazip.com/",
              "https://ip.cn/",
              "https://httpbin.org/ip"]

# Router config
url_route = "" # url of gateway login
url_wan = "" # url of infomation with WAN
login_data = {'username':'',
                'psd':''} # account and password for router login

class ObtainIP:
    def Get_ip(self):
        i = 0
        while True:
            try:
                current_ip = self.get(url_source[i])
                print("Obtain IP from %s"%url_source[i])
                return current_ip
            except Exception as ex:
                print("Ops Current Error : %s.\n Try other source to obtain public IP..."%ex)
                if i == (len(url_source) - 1):
                    current_ip = self.get_wan()
                    print("Obtain IP from WAN.")
                    return current_ip
                else:
                    i += 1
                    pass

    def get(self,url):
        '''
        :param url: request target url
        :return: a list with public ip
        '''
        response_data = requests.get(url=url).content
        ip = re.findall(r"(?<![\.\d])(?:25[0-5]\.|2[0-4]\d\.|[01]?\d\d?\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)(?![\.\d])",response_data.decode())
        return ip

    def get_wan(self):
        '''
        :return: obtain public IP from router WAN
        '''
        url = url_route
        data = login_data
        session = requests.Session()
        session.post(url=url,data=data)
        response_data = session.get(url=url_wan).text
        WAN_ip = json.loads(response_data)["WANIP"]
        return WAN_ip

def Verify_Network():
    loop_count = 0
    while True:
        try:
            url = "https://www.baidu.com"
            response = requests.get(url = url)
            return response.status_code
        except Exception as ex:
            print("Error happen as %s.\n Waiting for network ..."%ex)
            time.sleep(5)
            loop_count += 1
            if loop_count < 10:
                pass
            else:
                return 400

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

def Mail_inform(ip):
    From_addr = sender
    pwd = password
    To_addr = receiver
    smtp_server = SMTP_server
    mail_content = content + str(ip)

    msg = MIMEText(mail_content, 'plain', 'utf-8')
    msg['From'] = _format_addr('Python-Tool <%s>' % From_addr)
    msg['To'] = _format_addr('User <%s>' % To_addr)
    msg['Subject'] = Header(subject, 'utf-8').encode()

    server = smtplib.SMTP_SSL(smtp_server,465)
    server.ehlo(sender)
    if server.has_extn('STARTTLS'):
        server.starttls()
    server.ehlo(sender)
    server.set_debuglevel(1)
    server.login(From_addr, pwd)
    server.sendmail(From_addr, [To_addr], msg.as_string())
    server.quit()
    return 0

if __name__ == '__main__':
    code = Verify_Network()
    if code == 200:
        print("Network is smooth.")
        Obtain_tool = ObtainIP()
        ip = Obtain_tool.Get_ip()
        try:
            Mail_inform(ip)
            print("E-mail sends successfully.")
        except smtplib.SMTPException as e:
            print("error %s.")
    else:
        print("error code %s and program stopped."%code)