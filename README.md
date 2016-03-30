### 功能： ###

从 **[cspo内网通知栏](http://cspo.zju.edu.cn/redir.php?catalog_id=21530)**上抓**读书报告**的通知

抓到读书报告的通知后，会**发一个邮件到用户设定的邮箱**

### 说明: ###
1. 邮件需要支持SMTP协议，并使用默认端口25，如果想手动修改，在sendMail函数中，修改`s = smtplib.SMTP(host, timeout=5)`
2. 建议在不关机的server上写个脚本，2~3天执行一次这个文件
3. 默认使用明文的写密码的...为了方便在服务器上跑...如果想手动跑的话，把	`hand_input_passwd = False` 改为 True



### 使用配置方法： ###
	
在函数`sendMail():`里：

参数|说明
---|---
sender | 发送者 
receiver| 收件人
_pwd | 密码 
host | smtp的主机（默认使用浙大邮箱）
subject|主题
 

### 运行要求： ###
	python ==> version 3.x

### Packages: ###
	pyquery ==> 1.2.11

# 主要是自己用，鲁棒性和安全性都比较低，欢迎改进 #



