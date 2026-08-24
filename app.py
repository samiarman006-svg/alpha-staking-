from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>ALPHA Staking</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background: #0b1020;
                color: white;
                text-align: center;
            }

            .header {
                padding: 25px;
                background: #151d38;
                font-size: 28px;
                font-weight: bold;
            }

            .card {
                max-width: 420px;
                margin: 60px auto;
                padding: 30px;
                background: #151d38;
                border-radius: 18px;
            }

            .btn {
                display: inline-block;
                padding: 13px 25px;
                margin-top: 20px;
                background: #2563eb;
                color: white;
                text-decoration: none;
                border-radius: 10px;
            }
        </style>
    </head>

    <body>
        <div class="header">ALPHA</div>

        <div class="card">
            <h1>ALPHA Staking</h1>
            <p>USDT Staking Platform</p>
            <p>Welcome to ALPHA</p>

            <a class="btn" href="#">Get Started</a>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run() 
