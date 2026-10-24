from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "FF Like Bot is Running! Use /like?uid=YOUR_UID"

@app.route('/like')
def like():
    uid = request.args.get('uid')
    if not uid:
        return jsonify({"error": "UID dao! ?uid=123456789"}), 400
    
    # Free Fire Like API (example)
    try:
        # Ekhane asol API bosabe
        url = f"https://ff-like-api.vercel.app/like?uid={uid}"
        r = requests.get(url)
        return jsonify({
            "status": "Success",
            "uid": uid,
            "result": r.json()
        })
    except Exception as e:
        return jsonify({"status": "Error", "message": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
