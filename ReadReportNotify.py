#coding:utf-8
from pyquery import PyQuery as pq 
import urllib.request
import urllib.parse
import os.path
import pickle
import smtplib
from email.mime.text import MIMEText  

hand_input_passwd = False

def sendMail(content = '读书报告的通知邮件', passwd = '123'):
	sender = '发送者邮箱'
	receiver = '收件人邮箱'
	if hand_input_passwd:
		_pwd = passwd
	else:
		_pwd = '发送者密码'
	
	host = 'smtp.zju.edu.cn'
	subject = '读书报告'
	msg = MIMEText(content)  
	msg['Subject'] = subject
	msg['From']    = sender 
	msg['To']      = receiver
	try:
		s = smtplib.SMTP(host, timeout=5)
		s.login(sender, _pwd)
		s.sendmail(sender, receiver, msg.as_string())
		s.close()  
	except smtplib.SMTPException:
		print('Error: Unable to send Notify mail')


url = 'http://cspo.zju.edu.cn/redir.php'
values = {'catalog_id':'21530'}
data = urllib.parse.urlencode(values).encode('utf-8')
req = urllib.request.Request(url, data)
response = urllib.request.urlopen(req)
page = response.read().decode('gb2312')

d = pq(page)
#WARNING: bad robust !!! here
doc = d('table[width="720"]').eq(2)('a.header-yz')
links = []
titles = []
for i in range(len(doc)):
	link = doc.eq(i).attr('href')
	links.append(link)
	title = doc.eq(i).html().strip()
	titles.append(title)

log_name = 'old_link.log'
if not os.path.isfile(log_name):
	with open(log_name, 'wb') as f:
		pickle.dump(links, f)
	print('It\'s the FIRST TIME you use, only the FILE: "old_link.log" will be created!')

with open( log_name, 'rb') as f:
	old_links = pickle.load(f)

update = False
toSend = ''
for i in range(len(links)):
	if links[i] not in old_links:
		url = 'http://cspo.zju.edu.cn/'+links[i]
		req = urllib.request.Request(url)
		response = urllib.request.urlopen(req)
		page = response.read().decode('gb2312')
		if '读书报告' in page:
			toSend =toSend + str(i)+'. '+titles[i]+'\nhttp://cspo.zju.edu.cn/'+links[i]+'\n'
		update = True

if not (toSend==''):
	if hand_input_passwd:
		passwd = input('输入邮件密码')
		sendMail(toSend, passwd)
	else:
		sendMail(toSend)
	
if update:
	with open(log_name, 'wb') as f:
		pickle.dump(links, f)


