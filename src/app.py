import time, os
from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/health')
def health_check():
    # DB PASS chk
    db_password = os.getenv('DB_PASSWORD')
    
    if not db_password:
        return jsonify({"status": "ERROR", "message": "Secret DB_PASSWORD is missing!"}), 500

    print(f"Connecting to DB with secret: {db_password[:2]}***")

    # DB response
    time.sleep(1)
    return jsonify({"status": "UP", "database": "connected"}), 200

if __name__ == '__main__':
    app.run(debug=True)
