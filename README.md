# Linux Servers course project: LAMP stack setup with example Python/Flask app

This is my final project for Haaga-Helia's **Linux Servers** course. The project involves deploying a LAMP stack (Linux, Apache, MySQL, Python) using [Ubuntu Server 22.04 LTS](https://ubuntu.com/download/server) on a virtual machine. The project includes an example Python/Flask web app that interacts with a MySQL database to demonstrate the functionality.

# App setup

Make sure you have **Python** and **pip** installed on your system. Follow these steps to set up and run the Flask app:

1. Install requirements:
```
pip install -r requirements.txt
```

2. Run the Flask app:
```
cd app
python app.py
```

3. Access the app in your web browser at `http://localhost:5000/`

# Sources

Using Flask and Jinja2 templates:
- https://flask.palletsprojects.com/en/stable
- https://www.youtube.com/watch?v=4yaG-jFfePc