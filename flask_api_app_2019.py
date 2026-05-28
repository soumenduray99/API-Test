
from flask import Flask, jsonify
import json

app = Flask(__name__)

with open('global_superstore_2019_api_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

@app.route('/')
def home():
    return jsonify({
        'message': 'Global Superstore 2019 API Running',
        'endpoints': [
            '/api/data',
            '/api/tables'
        ]
    })

@app.route('/api/data')
def get_all_data():
    return jsonify(data)

@app.route('/api/tables')
def get_tables():
    return jsonify(list(data.keys()))

@app.route('/api/table/<table_name>')
def get_table(table_name):
    if table_name in data:
        return jsonify(data[table_name])
    return jsonify({'error': 'Table not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
