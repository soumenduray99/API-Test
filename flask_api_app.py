
from flask import Flask, jsonify
import json

app = Flask(__name__)

with open("global_superstore_api_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

@app.route("/api/data", methods=["GET"])
def get_all_data():
    return jsonify(data)

@app.route("/api/tables", methods=["GET"])
def get_tables():
    return jsonify(list(data.keys()))

@app.route("/api/table/<table_name>", methods=["GET"])
def get_table(table_name):
    if table_name in data:
        return jsonify(data[table_name])
    return jsonify({"error": "Table not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
