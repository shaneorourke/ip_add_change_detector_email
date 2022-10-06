import smtplib 

def send_email(smtp_login,smtp_pw,sender,recipient,message):
    try: 
        #Create your SMTP session 
        smtp = smtplib.SMTP('smtp.gmail.com', 587) 

       #Use TLS to add security 
        smtp.starttls() 

        #User Authentication 
        smtp.login(smtp_login,smtp_pw)

        #Sending the Email
        smtp.sendmail(sender,recipient,message) 

        #Terminating the session 
        smtp.quit() 
        print ("Email sent successfully!") 

    except Exception as ex: 
        print("Something went wrong....",ex)
