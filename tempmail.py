def mail():
    import pyperclip
    import requests
    import random
    import string
    import time
    import sys
    import re
    import os

    base_url = 'https://www.1secmail.com/api/v1/'
    domainList = ['1secmail.com']
    domain = random.choice(domainList)

    def banner():
        print(r'''
                             ''~``
                            ( o o )
    +------------------.oooO--(_)--Oooo.------------------+
    |                                                     |
    |            TEMPORARY Mail GENERATION TOOL            |
    |                    [21BIT049]                       |
    |                                                     |
    |                    .oooO                            |
    |                    (   )   Oooo.                    |
    +---------------------\ (----(   )--------------------+
                           \_)    ) /
                                 (_/
                                 
     =[===> 21BIT049 | https://github.com/Vignesh-SMV <===]= """
        ''')

    def generateUserName():
        name = string.ascii_lowercase + string.digits
        username = ''.join(random.choice(name) for i in range(10))
        return username

    def extract():
        getUserName = re.search(r'login=(.*)&', newMail).group(1)
        getDomain = re.search(r'domain=(.*)', newMail).group(1)
        return [getUserName, getDomain]

    # Got this from https://stackoverflow.com/a/43952192/13276219
    def print_statusline(msg: str):
        last_msg_length = len(print_statusline.last_msg) if hasattr(print_statusline, 'last_msg') else 0
        print(' ' * last_msg_length, end='\r')
        print(msg, end='\r')
        sys.stdout.flush()
        print_statusline.last_msg = msg

    def deleteMail():
        url = 'https://www.1secmail.com/mailbox'
        data = {
            'action': 'deleteMailbox',
            'login': f'{extract()[0]}',
            'domain': f'{extract()[1]}'
        }

        print_statusline("Disposing your email address - " + mail + '\n')
        req = requests.post(url, data=data)

    def checkMails():

        user_token = mail.split('@')[0]
        response = requests.get(base_url + f'?action=getMessages&login={user_token}&domain={domain}')
        messages = response.json()

        if len(messages) > 0:
            for message in messages:
                # Fetch the email content
                message_id = message['id']
                message_response = requests.get(
                    base_url + f'?action=readMessage&login={user_token}&domain={domain}&id={message_id}')
                message_data = message_response.json()

                # Print or process the email content
                print("Sender:", message_data['from'])
                print("Subject:", message_data['subject'])
                print("Date:", message_data['date'])
                print("Content:", message_data['textBody'])
                print("\n")
                exit()
                # Delete the email
                requests.post(base_url + '?action=deleteMessage',
                              data={'login': user_token, 'domain': domain, 'id': message_id})

    banner()
    userInput1 = input("\033[32m Do you wish to use to a custom domain name (Y/N): \033[0m").capitalize()

    try:

        if userInput1 == 'Y':
            userInput2 = input("\nEnter the name that you wish to use as your domain name: ")
            newMail = f"{base_url}?login={userInput2}&domain={domain}"
            reqMail = requests.get(newMail)
            mail = f"{extract()[0]}@{extract()[1]}"
            pyperclip.copy(mail)
            print("\nYour temporary email is " + mail + " (Email address copied to clipboard.)" + "\n")
            print(f"---------------------------- | Inbox of {mail}| ----------------------------\n")
            while True:
                checkMails()
                time.sleep(5)

        if userInput1 == 'N':
            newMail = f"{base_url}?login={generateUserName()}&domain={domain}"
            reqMail = requests.get(newMail)
            mail = f"{extract()[0]}@{extract()[1]}"
            pyperclip.copy(mail)
            print("\nYour temporary email is " + mail + " (Email address copied to clipboard.)" + "\n")
            print(f"---------------------------- |\033[32m  Inbox of {mail}   \033[0m| ----------------------------\n")
            while True:
                checkMails()
                time.sleep(5)

    except(KeyboardInterrupt):
        deleteMail()
        print("\nProgramme Interrupted")
        os.system('cls' if os.name == 'nt' else 'clear')







