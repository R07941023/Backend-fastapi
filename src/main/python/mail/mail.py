import smtplib
from email.mime.text import MIMEText

account = 'a5822358@gmail.com'
password = 'a840702B851129'
 
# 收信寄信人的資料
to_email = "a5822358business@gmail.com"
from_email = "a5822358@gmail.com"
 
# MIME text
message = "mail內容"
msg = MIMEText(message, "html")
msg["Subject"] = "mail主旨"
msg["To"] = to_email
msg["From"] = from_email
 
# 指定伺服器
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(account, password)
server.send_message(msg)
server.quit()