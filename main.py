from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/check_payment', methods=['GET'])
def check_payment():
    """Endpoint that returns the payment status."""
    return jsonify({"payment_status": True})

if __name__ == '__main__':
    # Run the server on localhost:5000
    app.run(debug=True)
