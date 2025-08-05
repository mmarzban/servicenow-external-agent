from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/install', methods=['POST'])
def install_software():
    data = request.json
    software = data.get('software')
    user = data.get('user')
    device = data.get('device')

    result = {
        "status": "success",
        "message": f"{software} has been successfully 'installed' on {device} for user {user}."
    }
    return jsonify(result), 200

@app.route('/')
def home():
    return "External AI Agent is live!"
