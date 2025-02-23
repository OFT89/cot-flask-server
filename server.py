from flask import Flask, jsonify, request

app = Flask(__name__)  # Questa è l'istanza dell'app Flask che Gunicorn cerca

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "Server Online!"})

@app.route("/send_forecast", methods=["POST"])
def send_forecast():
    data = request.json
    forecast_value = data.get("forecast_net_positions")

    if forecast_value:
        return jsonify({"status": "Received", "forecast": forecast_value}), 200
    else:
        return jsonify({"error": "No forecast data"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
