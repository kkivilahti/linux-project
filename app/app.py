import os
from flask import Flask, render_template, redirect, request
import mysql.connector

app = Flask(__name__)

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database="guestbook"
    )

@app.route('/', methods=['GET', 'POST'])
def index():
    con = connect_db()
    cursor = con.cursor(dictionary=True)

    # If method is POST, either insert a new message or delete an existing one
    if request.method == 'POST':
        data = request.form

        if data.get('delete_id'):
            # If delete_id is present, delete the chosen message
            cursor.execute("DELETE FROM messages WHERE id = %s", (data['delete_id'],))
        else:
            # Otherwise, insert a new message
            name = data['name']
            msg = data['msg']
            cursor.execute("INSERT INTO messages (name, message) VALUES (%s, %s)", (name, msg))
        
        con.commit()
        cursor.close()
        con.close()
        return redirect("/")

    else:
        # If method is GET, fetch all messages to display
        cursor.execute("SELECT id, name, message FROM messages")
        messages = cursor.fetchall()

        cursor.close()
        con.close()

        return render_template('index.html', messages=messages)

if __name__ == "__main__":
    app.run(debug=True)