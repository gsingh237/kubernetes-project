#service2.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def service2():
    return "Hello, This is Service2 Response!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)