from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start():
    return jsonify({"message": "Step counting started"})

@app.route('/stop', methods=['POST'])
def stop():
    return jsonify({"message": "Step counting stopped"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=10000)
