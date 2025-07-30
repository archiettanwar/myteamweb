import ssl,smtplib
def sendemail(username,msg):
    password="bvam ukgr tynh mjjd"

    host="smtp.gmail.com"
    port=465
    toemail="archiettanwar71@gmail.com"

    context=ssl.create_default_context()

    with smtplib.SMTP_SSL(host,port,context=context) as server:
        server.login(toemail,password)
        server.sendmail(username,toemail,msg)