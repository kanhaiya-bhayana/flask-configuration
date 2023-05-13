from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('login.html')

@app.route('/form_login',methods=['POST','GET'])
def login():
    res = request.form['hola']
    if res != " ":
        return render_template('dashboard.html', hola=res)

if __name__ == '__main__':
    app.run()