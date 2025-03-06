from flask import Flask, jsonify, request
import json

app = Flask(__name__)

API_KEYS = ["j5a!20kqa7s9821"]

def load_stock_data():
    try:
        with open("real_time_stock_data.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return jsonify({"error": "Data Not Found"})

@app.route("/api/stocks", methods=["GET"])
def get_stocks():
    api_key = request.headers.get("X-API-KEY")

    # ✅ Check if API key is valid
    if api_key not in API_KEYS:
        return jsonify({"error": "Invalid API Key"}), 401
    
    stock_data = load_stock_data()
    return jsonify(stock_data)

if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")  
