from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
        <head>
            <style>
                body {
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    background-color: #f4f4f4;
                    font-family: Arial, sans-serif;
                }
                h1 {
                    font-size: 3em;
                    color: #333;
                    text-align: center;
                    background: linear-gradient(45deg, #ff5733, #ffbd69);
                    -webkit-background-clip: text;
                    -webkit-text-fill-color: transparent;
                }
            </style>
        </head>
        <body>
            <h1>Hello from Dockerized Flask App!</h1>
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)