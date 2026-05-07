from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return {
        "message": "Hello from my DevOps Project!",
        "status": "running",
        "environment": os.getenv("ENV", "production")
    }

@app.route('/health')
def health():
    return {"status": "healthy"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
