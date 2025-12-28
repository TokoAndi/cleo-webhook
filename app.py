from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Cleo Webhook OK"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print(data)  # buat ngecek dulu
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run()
