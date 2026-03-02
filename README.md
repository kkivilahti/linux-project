# Linux Servers course project: LAMP stack setup with example Python/Flask app

This is my final project for Haaga-Helia's **Linux Servers** course. The project involves deploying a LAMP stack (Linux, Apache, MySQL, Python) using [Ubuntu Server 22.04 LTS](https://ubuntu.com/download/server) on a virtual machine. The project includes an example Python/Flask web app that interacts with a MySQL database to demonstrate the functionality.

# App setup

Make sure you have **Python**, **pip** and **MySQL Server** installed on your system.

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

# Sources

Using Flask and Jinja2 templates:
- https://flask.palletsprojects.com/en/stable
- https://www.youtube.com/watch?v=4yaG-jFfePc

Using MySQL with Python:
- https://www.youtube.com/watch?v=14HTiBQEQ9M
- https://www.geeksforgeeks.org/python/python-mysql/