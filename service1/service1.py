#service1.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def service1():
    return "Hello, This is Service1 Response!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)