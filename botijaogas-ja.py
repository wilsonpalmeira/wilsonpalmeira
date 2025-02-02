from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('botijaogas-ja.html')

if __name__ == '__main__':
    app.run(debug=True)
# gunicorn myapp:app 
# servidor do render.com
# https://github.com/wilsonpalmeira/botijaogas-ja.git
