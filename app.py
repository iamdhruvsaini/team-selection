from flask import Flask, request, jsonify
from flask_cors import CORS
from optimizer import find_best_team

app = Flask(__name__)
CORS(app)  # Allow requests from any origin

@app.route('/api/optimize', methods=['POST'])
def optimize():
    
    try:
        data = request.get_json()
        if not data:
            return jsonify({"success": False, "message": "No input data provided"}), 400
        
        # Call optimizer function
        result = find_best_team(data)
        return jsonify({"success": True, "data": result}), 200

    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
