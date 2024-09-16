import smtplib as s

a= s.SMTP("smtp.gmail.com",587)
a.ehlo()
a.starttls()
print("Enter your Credential Please for Sending Email")
email = input("Enter your Email Adress: ")
password = input("Enter your Password: ")

try:
    try:
        a.login(email,password)
        print("Login Successful")
    except Exception as e:
        print("Invalid Email or Password")
    finally:
        a.quit()

    subject = 'Test the main server'
    body = "Hello, this is a test email sent using Python's smtplib module."
    message = "subject:{}\n\n{}".format(subject,body)
    SenderList = ["123@gmail.com",
                "456@gmail.com",
                "789@gmail.com"  # Add more recipients here if needed
    ]
    a.sendmail(email,"recipient_email@gmail.com | the list created",message)
    a.quit()
    print("Email sent successfully!")
    print("Check your inbox for the email.")
except Exception as e:
    print("Error sending email:", e)



