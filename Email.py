import smtplib
import config

def send_mail(customer_email, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)
        message = "subject: Top 10 restaurants \n\n{}".format(msg)
        server.sendmail(config.EMAIL_ADDRESS, str(customer_email), message)
        server.quit()
        print('Mail Delivery-Success to ',customer_email)
    except:
        print('Mail Delivery-Failed')
