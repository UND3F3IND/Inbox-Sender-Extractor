import imaplib
import time
from colorama import Fore, Style


print(f'''
{Fore.CYAN}
██    ██ ███    ██ ██████  ██████  ███████ ██████  ██ ███    ██ ██████  
██    ██ ████   ██ ██   ██      ██ ██           ██ ██ ████   ██ ██   ██ 
██    ██ ██ ██  ██ ██   ██  █████  █████    █████  ██ ██ ██  ██ ██   ██ 
██    ██ ██  ██ ██ ██   ██      ██ ██           ██ ██ ██  ██ ██ ██   ██ 
 ██████  ██   ████ ██████  ██████  ██      ██████  ██ ██   ████ ██████  


{Style.RESET_ALL}''')


while True:
    email = input(f"{Fore.YELLOW}Enter your email: {Style.RESET_ALL}")
    password = input(f"{Fore.YELLOW}Enter your password: {Style.RESET_ALL}")
    mail = imaplib.IMAP4_SSL('imap-mail.outlook.com')
    try:
        mail.login(email, password)
        break
    except imaplib.IMAP4.error:
        print(f"{Fore.RED}Incorrect email or password. Please check your details and try again.{Style.RESET_ALL}")

# Select the Inbox folder
mail.select('INBOX')
typ, msgnums = mail.search(None, 'ALL')
senders = set()
num_lines_found = 0
animation = "|/-\\"
i = 0
print(f"{Fore.GREEN}Processing, please wait...{Style.RESET_ALL}")
for num in msgnums[0].split():
    typ, msgdata = mail.fetch(num, '(BODY[HEADER.FIELDS (FROM)])')
    for response_part in msgdata:
        if isinstance(response_part, tuple):
            sender = response_part[1].decode().split(": ", 1)[1].strip()
            senders.add(sender)
            num_lines_found += 1
    print(f"{Fore.GREEN}Processing: {animation[i % len(animation)]} Please wait...{Style.RESET_ALL}", end="\r")
    i += 1
    time.sleep(0.1)

mail.close()
mail.logout()
file_name = input(f"{Fore.YELLOW}Enter the name of the file to save the senders: {Style.RESET_ALL}")

with open(file_name, 'w') as f:
    f.write('\n'.join(senders))
print(f"{Fore.GREEN}Number of inbox senders: {num_lines_found}")
print(f"Senders saved to file: {file_name}{Style.RESET_ALL}")
