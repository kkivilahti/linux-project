# Linux Servers course project: LAMP stack setup with example Python/Flask app

This is my final project for Haaga-Helia's **Linux Servers** course. The project involves deploying a LAMP stack (Linux, Apache, MySQL, Python) using [Ubuntu Server 22.04 LTS](https://ubuntu.com/download/server) on a virtual machine. The project includes an example Python/Flask web app (guestbook) that interacts with a MySQL database to demonstrate the functionality.


# What is a LAMP stack?

A LAMP stack is a common web development platform that consists of the following components:
- **Linux**: The operating system that serves as the foundation for the stack.
- **Apache**: The web server that handles HTTP requests and serves web content to users.
- **MySQL**: The relational database management system that stores and manages data for the web application.
- **Python**: The programming language used to develop the web application, often paired with a framework like Flask or Django. (Other popular languages for LAMP stacks include PHP and Perl, but in this project I will be using Python.)


# App setup (locally)

The example app is a simple guestbook where users can submit their name and a message, which are then stored in a MySQL database and displayed on the page. The app is built using Flask.

Before running the app, make sure you have **Python**, **pip** and **MySQL Server** installed on your system.

First, clone the repository and navigate to the project directory. Then follow these steps to set up and run the app:

1. Install requirements:
```
pip install -r requirements.txt
```

2. Set up the MySQL database:
- Change the db username and password as needed. Make sure to update both the `app/schema.sql` file and the `.env` file with the same credentials
- Example `.env` file:
```
DB_USER=guestuser
DB_PASSWORD=password
```

- Log in to MySQL and initialize the database by running the following command in your terminal:
```
mysql -u root -p < app/schema.sql
```
Note: root is the default MySQL user. If you have a different user, replace `root` with your MySQL username.

3. Start the app:
```
python app/app.py
```

4. Access the app in your browser at `http://localhost:5000/` (or the address displayed in your terminal)


# App setup (on Ubuntu Server)

Start up your Ubuntu Server VM and log in. Then follow these steps to set up the LAMP stack and deploy the app:

1. First update the package lists and install Apache web server:
```
sudo apt update
sudo apt install apache2
```

Note: you might need to update your VM's network settings. I'm using a bridged adapter, which allows the VM to have its own IP address on the local network. You can find the VM's IP address by running `ip addr` in the terminal. Then you can test the server by navigating to `http://<IP_ADDRESS>/` in your browser (you should see the Apache2 Ubuntu Default Page).

2. Install required packages for the application:
```
sudo apt install python3 python3-pip python3-venv mysql-server libapache2-mod-wsgi-py3 git
```

3. Navigate to `/var/www` and clone the repository there:
```
cd /var/www
sudo git clone https://github.com/kkivilahti/linux-project.git
```
Note: when using https to clone the repository, you might be prompted to enter your GitHub credentials. If you have two-factor authentication enabled, you will need to use a personal access token INSTEAD of your password.

You can create a personal access token in your GitHub account settings under `Developer settings` > `Personal access tokens`. Make sure to give the token appropriate permissions (like repo access) and use it as the password when prompted during the git clone process.

To work *without sudo* in the project directory, you can change the ownership of the directory to your user:
```
sudo chown -R $USER:$USER /var/www/linux-project
```

4. Set up the Python virtual environment and install requirements:
```
cd linux-project
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

5. Set up the MySQL database:
- Log in to MySQL and initialize the database by running the following command in your terminal:
```
sudo mysql -u root -p < app/schema.sql
```
Note: root is the default MySQL user. If you have a different user, replace `root` with your MySQL username.

Open the MySQL monitor and test the connection:
```
sudo mysql
mysql> USE guestbook;
mysql> SELECT * FROM messages;
```
At this point you should see an empty result set, since there are no messages in the database yet.

6. Create a WSGI file for the app:
```
nano /var/www/linux-project/wsgi.py
```

Add the following content to the file:
```
import sys

sys.path.insert(0, '/var/www/linux-project')

from app.app import app as application
```

TODO: explain the WSGI file and add the next steps for configuring Apache to use it. Also add instructions for setting up the .env file on the server and explain how to keep it secure
7. Configure Apache settings for the app

8. Restart Apache to apply the changes

9. Access the app in your browser at `http://<IP_ADDRESS>/` (replace `<IP_ADDRESS>` with your VM's IP address)

# Sources

What is a LAMP stack?
- https://www.youtube.com/watch?v=tzBgFog6NmY

Using Flask and Jinja2 templates:
- https://flask.palletsprojects.com/en/stable
- https://www.youtube.com/watch?v=4yaG-jFfePc

Using MySQL with Python:
- https://www.youtube.com/watch?v=14HTiBQEQ9M
- https://www.geeksforgeeks.org/python/python-mysql/

Installing Apache Web Server on Ubuntu:
- https://www.digitalocean.com/community/tutorials/how-to-install-the-apache-web-server-on-ubuntu-22-04

Deploying a Flask app using Linux, Apache and WSGI:
- https://www.youtube.com/watch?v=w0QDAg85Oow
- https://medium.com/@farhanahmedindia/complete-guide-deploying-a-flask-app-on-apache-ubuntu-c2f5d7b17e20