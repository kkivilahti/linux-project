-- use this file to initialize the MySQL database
CREATE DATABASE IF NOT EXISTS guestbook;
USE guestbook;

-- change username and password as neded
-- make sure they match the credentials in the .env file
CREATE USER IF NOT EXISTS 'guestuser'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON guestbook.* TO 'guestuser'@'localhost';

CREATE TABLE IF NOT EXISTS messages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    message TEXT NOT NULL
);