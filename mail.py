#rieibayqojnoihpk
def send_mail(sub, mail_message, file=None):
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    from email.header import Header
    import smtplib
    import os

    user = 'ajaymaurya5753@gmail.com'
    app_password = 'rieibayqojnoihpk'
    host = 'smtp.gmail.com'
    port = 465
    to = 'ajaycook46@gmail.com'

    subject = sub
    content_txt = mail_message
    attachment = file

    ### Define email ###
    message = MIMEMultipart()
    # add From 
    message['From'] = Header(user)
    # add To
    message['To'] = Header(to)     
    # add Subject
    message['Subject'] = Header(subject)
    # add content text
    message.attach(MIMEText(content_txt, 'plain', 'utf-8'))
    # add attachment
    att_name = os.path.basename(attachment)
    att1 = MIMEText(open(attachment, 'rb').read(), 'base64', 'utf-8')
    att1['Content-Type'] = 'application/octet-stream'
    att1['Content-Disposition'] = 'attachment; filename=' + att_name
    message.attach(att1)
        
    ### Send email ###
    server = smtplib.SMTP_SSL(host, port) 
    server.login(user, app_password)
    server.sendmail(user, to, message.as_string()) 
    server.quit() 
    print('Sent email successfully')  


if __name__ =="__main__":
    send_mail("test","hello", 'data/mic.png')