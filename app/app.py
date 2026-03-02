from flask import Flask, render_template, redirect, request
import uuid

app = Flask(__name__)

messages = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.form

        if data.get('delete_id'):
            for i in range(len(messages)):
                if messages[i].get('id') == data['delete_id']:
                    del messages[i]
                    break
        else:
            name = data['name']
            msg = data['msg']
            messages.append({
                "id": str(uuid.uuid4()),
                "name": name,
                "msg": msg
            })
        
        return redirect("/")

    else:
        return render_template('index.html', messages=messages)

if __name__ == "__main__":
    app.run(debug=True)