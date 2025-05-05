from flask import Flask, request, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Replace these with your actual RDS/PostgreSQL credentials
DB_HOST = "db-sarvar.ct6ei6agkus4.ap-south-1.rds.amazonaws.com"
DB_NAME = "db_sarvar"
DB_USER = "postgres"
DB_PASSWORD = "postgres"

def get_connection():
    return psycopg2.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

@app.route('/contracts', methods=['GET'])
def get_contracts():
    conn = get_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM tbl_sarvar_contracts ORDER BY id")
    results = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(results)

@app.route('/contracts', methods=['POST'])
def add_contract():
    data = request.get_json()
    name = data.get('name')
    amount = data.get('amount')

    if not name or not amount:
        return jsonify({"error": "Missing 'name' or 'amount'"}), 400

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_sarvar_contracts (name, amount) VALUES (%s, %s) RETURNING id", (name, amount))
    new_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"message": "Contract added", "id": new_id}), 201

@app.route('/contracts/<int:contract_id>', methods=['DELETE'])
def delete_contract(contract_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM tbl_sarvar_contracts WHERE id = %s RETURNING id", (contract_id,))
    deleted = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()

    if deleted:
        return jsonify({"message": f"Contract {contract_id} deleted"}), 200
    else:
        return jsonify({"error": "Contract not found"}), 404

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)
