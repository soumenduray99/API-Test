
from flask import Flask, jsonify
import json

app = Flask(__name__)

with open('tableau_final_fixed_api_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

@app.route('/')
def home():
    return jsonify({
        'message': 'Tableau Compatible API Running',
        'status': 'success',
        'routes': {
            'all_data': '/api/data',
            'tables': '/api/tables',
            'orders': '/api/table/Orders',
            'returns': '/api/table/Returns',
            'people': '/api/table/People'
        }
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
