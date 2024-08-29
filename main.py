import smtplib

my_email = "nawal.nadeem@gmail.com" #sender's email
password = "pkkv fdml trkn fmhu" # sender email's passowrd generated at Gmail app passwords page
connection = smtplib.SMTP("smtp.gmail.com")
#smtp different for each email provider
# hotmail --- smtp.live.com
# yahoo -- smtp.mail.yahoo.com
# gmail -- smtp.gmail.com

connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(
    from_addr=my_email,
    to_addrs="nawal.nadeem@gmail.com" #Recipient's email address. Multiple email ids can be added separated by commas
    msg="Subject: Hello \n\n This is the body of my email."
)
connection.close()
