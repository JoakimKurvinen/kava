#sendmail part
recipient = "kahviparina@mailinator.com" #email is inputed by the user
subject = "The temperature is reached o' Master"
body = 'The temperature you set for your beverage has been reached'

def send_email(recipient, subject, body):
          try:
              process = subprocess.Popen(['mail','-s',subject,recipient],stdin=subprocess.PIPE)
          except Exception, error:
              print error
          process.communicate(body)

          send_message(recipient, subject, body)

          print("sent the email")
