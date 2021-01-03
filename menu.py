from helper import *
from password import *
import sys, os

#system = sys.platform
#cmd = 'clear' if sys.platform == 'linux' else 'cls'

first= '''
1. Login
2. Sing Up
Q. Quit
'''
second = '''
1. Add new password
2. Show password for an app or site
3. Show names of all your the apps
4. Delete Record
5. Logout
6. Generate Password for an app
Q. quit
'''


def call_login():
    do = True
    while do:

        user_id,password = login(conn)

        if isinstance(user_id, int):
            print('\t'+color['OKGREEN']+color['UNDERLINE']+'logged in'+color['ENDC'])
            do = False
            return user_id, password

        else:
            print(user_id)


def login_singup():
    while True:
        print(first)
        choice = input('Choice: ')
        if choice[0].lower() == 'q':
            sys.exit()

        elif choice == '1':
            return call_login()
        
        elif choice == '2':
            print(signup(conn, input('Choose Username: ')))
        #os.system(cmd)

def menu():
    global user_id
    while user_id:
        print(second)
        choice = input('Choice: ')

        if choice[0].lower() == 'q':
            sys.exit()

        elif int(choice) == 1:
            add_password(conn, user_id ,input('App Name: '), getpass.getpass('Add password: '), password)

        elif int(choice) == 2:
            get_password(conn, user_id, input('App Name: '), password)

        elif int(choice) == 3:
            all_apps(conn, user_id)

        elif int(choice) == 4:
            print(delete(conn, input('App name: '), user_id))
            
        elif int(choice) == 5:
            del user_id
            print('Loging out')
            return
        elif int(choice) == 6:
            app_password = password_generator()
            app_name = input('App Name: ')
            add_password(conn, user_id ,app_name , app_password, password)
            get_password(conn, user_id,app_name , password)
            

        #os.system(cmd)


while True:
    user_id, password = login_singup()
    menu()
