import datetime
import jarvis as jv
import smtplib   # this module is used to send email through gmail but for that you have to 
import json
import pywhatkit

def wishMe():
    '''
    This function can greet you as per time 
    '''
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <12:
        jv.speak("Good Morning Sir!")
    elif hour >= 12 and hour <18:
        jv.speak("Good Afternoon Sir!")
    else :
        jv.speak("Good Evening Sir!")


def sendEmail(to,content):
    '''
    This function takes two argument sendEmail(email_address,content to be send..) 
    And send the email to the person whose argument is read with the content 
    which is also read form the parameters
    '''
    with open("data.json") as f:
        data = json.load(f)       
        mailAdd = data[to]["email"]                     # here it will find the mail of person which is given to it in json file
        
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    with open('D:\\Riyank\\project\\jarvis\\password.txt','r') as f: 
        passcontent = f.read()                                                 # passcontent is email password that is used to send the mail
    server.login('rajmalhotra7086@gmail.com',passcontent)
    server.sendmail('rajmalhotra7086@gmail.com',mailAdd,content)
    server.close()


def sendMsgWhatsapp(person,msg):
    """
    This function takes two argument sendMsgWhatsapp(person name or phone number,content to be send..) 
    And send the message to the person whose argument is read with the content 
    which is also read form the parameters  
    """
    hr = datetime.datetime.now().hour
    mnt = datetime.datetime.now().minute
    with open("data.json") as f:
        data = json.load(f)       # here it will find the number of person which is given to it in json file
        phone_num=data[person]["phone"]             

    try:
        pywhatkit.sendwhatmsg(phone_num,msg,hr,mnt+1)
        speak("Message has been sent Successfully!")
        print("Message has been sent Successfully!")

    except :
            print("An Unexpected Error!")
    

def write_json(data,filename="data.json"):
    """
    This function generally takes the data and store it to the specific json file
    """
    with open(filename,"w") as f :
        json.dump(data, f,indent=4)

def saveEmail(email,key):
    """
    This function takes two argument, the first is email address that want to save
    and the other is key or person's name that the email of,and both the arguments are string
    saveEmail('123@gmail.com','riaynk')  
    and send it to the write_json function 
    """
    with open("data.json") as f:
        data = json.load(f)
        if key in data.keys():
            e = {"email":email}
            data[key].update(e)


        else : 
            y = {key:{
                "email":email
            }}
            data.update(y)
    data=sorted(data.items())
    data=dict(data)
    write_json(data)

def savePhoneNumber(phone,key):
    """
    This function takes two argument, the first is mobile number that want to save
    and the other is key or person's name that the mobile number of,and both the arguments are string
    saveEmail('+919837263727','riaynk')  
    and send it to the write_json function 
    """
    phone_num = "+91"+phone
    with open("data.json") as f:
        data = json.load(f)
        
    if key in data.keys():
        p = {"phone":phone_num}
        data[key].update(p)
    else :
        y = {key:{
            "phone":phone_num
        }}
        data.update(y)
    data=sorted(data.items())
    data=dict(data)
    write_json(data)

def checkPassword(password):
    """"
    it checks the passsword with the password store in the json file 
    """
    with open('data.json') as f :
        data = json.load(f)

    p = data["password"]
    if password == p:
        return True
    else :
        return False

def setPassword(password):
    """
    it strores the new password in the json file 
    """
    with open('data.json') as f :
        data = json.load(f)

    data["password"] = password
    write_json(data)
    