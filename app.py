from flask import Flask

app = Flask(__name__)

@app.route('/')
def route():
    return 'Hola mundo!'

@app.route('/test')
def test():
    return 'Estamos en test!'

if __name__ == '__name__':
    app.run(debug=True)