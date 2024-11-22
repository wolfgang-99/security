from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the secure API "}), 200

@app.route('/check_payment', methods=['GET'])
def check_payment():
    """Endpoint that returns the payment status."""
    return jsonify({"payment_status": False})

if __name__ == '__main__':
    app.run(debug=True)
