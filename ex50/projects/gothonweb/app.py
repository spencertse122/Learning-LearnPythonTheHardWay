from flask import Flask
from flask import render_template

app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     # greeting = "World"
#     return f'Hello, {greeting}!'

@app.route('/')
def index():
    greeting = "HELL YEAH"
    listOfNumbers = [i for i in range(20)]
    return render_template("index.html",
                        greeting=greeting,
                        listOfNumbers=listOfNumbers)

if __name__ == '__main__':
    app.run()
