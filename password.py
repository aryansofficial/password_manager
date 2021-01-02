import mysql.connector, hashlib, getpass, cryptocode, pyperclip
from helper import color

def connection():
    '''Connect and return connection'''
    try:
        conn = mysql.connector.connect(
            host='127.0.0.1',
            user='pwmanager',
            password='pwpassword',
            database='pwmanager')
    except Exception as e:
        print(e)
        print(color['WARNING']+'\nDid You follow the instruction and run the .sql file?'+color['ENDC'])
        exit()
    return conn


def login(conn):
    '''login and returns the user_id'''

    username = input(color['OKBLUE']+'Username: '+color['OKCYAN'])
    password = getpass.getpass(f'[{username}]: ')
    enc_password = hashlib.sha256(password.encode()).hexdigest()
    sql = 'SELECT user_id FROM login WHERE user="'+username+'" AND password="'+enc_password+'"'

    cursor = conn.cursor()
    cursor.execute(sql)

    try:
        return cursor.fetchall()[0][0], password
    except:
        return color['WARNING']+'User name and password do not match'+color['ENDC'],'' 


def signup(conn, user):
    '''Adds a new account'''

    sql = "SELECT user FROM login WHERE user='"+user+"'"
    cursor = conn.cursor()
    cursor.execute(sql)

    if cursor.fetchall() != []:
        return f'\t{color["WARNING"]}Username {user} is taken{color["ENDC"]}'

    print(color['UNDERLINE']+'\nThis password will be used to encode all the password so make a strong one and relember it.\n'+color['ENDC'])
    password = hashlib.sha256((getpass.getpass(f'Password[{user}]: ').encode())).hexdigest()
    sql = 'INSERT INTO login(user, password) VALUES("'+user+'","'+password+'")'

    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()

    return 'Account added'


def add_password(conn, user_id ,app_name, add_password, user_password): # remove default user_password
    '''This will add app and password'''
    
    sql = 'SELECT app_name FROM password WHERE app_name= "'+app_name+'"'
    add_password = cryptocode.encrypt(add_password, user_password)
    cursor = conn.cursor()
    cursor.execute(sql)

    if cursor.fetchall() != []:
        sql = 'UPDATE password SET password = "'+add_password+ '" WHERE app_name = "'+app_name+'";'
        if input(color['WARNING']+'App name exists in database. Reqrite?(y/n): '+color['ENDC'])[0].lower() != 'y':
            return
        pass 
    else:
        sql = "INSERT INTO password(user_id,app_name, password, ini_date) VALUES('"+str(user_id)+"','"+app_name+"', '"+add_password+"', curdate());"
    
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()

    print(color['OKGREEN']+color['UNDERLINE']+'\tPassword Added'+color['ENDC'])


def get_password(conn, user_id, app_name, password):
    '''Gets the password and copies to cpliboard'''

    sql = "SELECT password FROM password WHERE user_id= '"+str(user_id)+"' AND app_name= '"+app_name+"' "
    cursor = conn.cursor()
    cursor.execute(sql)
    res = cursor.fetchall()

    print(color['WARNING']+'No password found by app name'+color['ENDC'] if res == [] else color['WARNING']+'Copied to Clip board'+color['ENDC'],end=' ')
    password = cryptocode.decrypt(res[0][0], password)

    print(f'{app_name} : {password}')
    pyperclip.copy(password)


def all_apps(conn, user_id):
    '''This will get all app names from database'''

    sql = "SELECT app_name FROM password WHERE user_id='"+str(user_id)+"'"
    cursor = conn.cursor()
    cursor.execute(sql)
    # print('Hello ')
    print()
    res = cursor.fetchall()
    print('No records found ' if len(res) == 0 else ''*32+'\n{0:^10} {1:^20}'.format('App Name', 'Password'))
    for num, i in enumerate(res):
        print(" {0:.<10}{1:.>20}".format(str(num+1)+'.', i[0]))


def delete(conn, app_name, user_id):
    if input(f'Are you sure you want to delete {app_name}\' password?(y/n): ')[0].lower() == 'y':
        sql = f'DELETE FROM password WHERE app_name="{app_name}" AND user_id="{user_id}"'
        cursor = conn.cursor()
        try:
            cursor.execute(sql)
            conn.commit()
        except Exception as e:
            print(e)
        return color['OKGREEN']+'\tRecord Deleted'+color['ENDC']
    else:
        return color['OKGREEN']+'\tAborted'+color['ENDC']


conn = connection()
