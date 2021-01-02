# password_manager
Python 3 password manager

To-Do and Requirnments:

  1) Login as root in mysql database & run the following commands.

    CREATE USER 'pwmanager'@'localhost' IDENTIFIED BY 'pwpassword';
    GRANT ALL PRIVILEGES ON pwmanager.* TO 'pwmanager'@'localhost';

  2) The python 3 requirnments
    
    sudo apt-get install python3-pip -y
    pip3 install mysql.connector
    pip3 install cryptocode


## Usage
After running all the above command
  
    python3 menu.py 
