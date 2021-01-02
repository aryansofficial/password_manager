DROP DATABASE IF EXISTS pwmanager;
CREATE DATABASE pwmanager;
USE pwmanager;
CREATE TABLE
DROP TABLE IF EXISTS login ;
CREATE TABLE login(
     user_id SMALLINT PRIMARY KEY AUTO_INCREMENT, -- SMALLINT
     user VARCHAR(20) NOT NULL,
     password VARCHAR(64) NOT NULL
);

DROP TABLE IF EXISTS password; 
CREATE TABLE password(
    password_id SMALLINT PRIMARY KEY AUTO_INCREMENT,
    user_id SMALLINT NOT NULL, -- SAMLLINT
    app_name VARCHAR(30) NOT NULL,
    password VARCHAR(150) NOT NULL,
    ini_date DATE,
    FOREIGN KEY(user_id) REFERENCES login(user_id)
);

#INSERT INTO password(user_id,app_name, password, ini_date) VALUES(1,'facebook.com', 'check', curdate());

#INSERT INTO login(user, password)
#VALUES('Aryan',(select sha1('password')));

#INSERT INTO login(user, password)
#VALUES('Aryan',(select sha1('password123')));
