from flask import Flask, request, jsonify
from scanner.utils import scan_all

app = Flask(__name__)

@app.route("/scan", methods=["POST"])
def scan():
    target_url = request.json.get("url")
    scan_all(target_url)
    return jsonify({"message": "Scan complete", "target": target_url})

if __name__ == "__main__":
    app.run(debug=True)
