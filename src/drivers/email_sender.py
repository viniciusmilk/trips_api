import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(to_addrs, body):
    from_addr = 'hthw6mmwctsswjt5@ethereal.email'
    login = 'hthw6mmwctsswjt5@ethereal.email'
    password = '8r469B1EAGQQhrGVTQ'

    msg = MIMEMultipart()
    msg['from'] = 'trip_confirm@email.com'
    msg['to'] = ', '.join(to_addrs)

    msg['Subject'] = 'Confirmação de Viagem'
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.ethereal.email', 587)
    server.starttls()
    server.login(login, password)
    text = msg.as_string()

    for email in to_addrs:
        server.sendmail(from_addr, email, text)
    
    server.quit()