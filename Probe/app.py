from flask import Flask
app = Flask(__name__)

@app.route('/health1')
def health():
    return "healthy", 200

@app.route('/ready1')
def ready():
    return "ready", 200

@app.route('/alive1')
def alive():
    return "alive", 200

@app.route('/')
def home():
    return "HeLlO ThIs Is FrOm PyThOn ApP", 200

app.run(host='0.0.0.0', port=80)