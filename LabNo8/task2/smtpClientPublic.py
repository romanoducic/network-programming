
import smtplib 
import email.utils

content = 'test message' 

content = smtplib.SMTP('smtp.gmail.com', 587)

mail.ehlo()
mail.starttls()
mail.login('email', 'password')

mail.sendmail('9r9o99@gmail.com', 'anteprojic@gmail.com', content)

mail.close()