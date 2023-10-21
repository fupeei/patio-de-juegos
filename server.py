from flask import Flask, render_template

app = Flask(__name__)

# http://127.0.0.1:5000 #

@app.route("/")
def hola():
    return "HOLA!"

@app.route("/play")
def jugar():
    return render_template('index.html')

@app.route("/play/<int:num>")
def cuantos(num):
    return render_template('cubos.html', num=num)

@app.route("/play/<int:num>/<string:color>")
def colores (num, color):
    return render_template('colorescubos.html', num=num, color=color)

if __name__ == "__main__":
    app.run(debug=True)