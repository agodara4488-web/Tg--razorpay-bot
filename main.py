from flask import Flask, request

app = Flask(_name_)

@app.route("/", methods=["GET"])
def index():
    return "Bot server running", 200

@app.route("/webhook-test", methods=["POST"])
def webhook_test():
    print("Got POST:", request.json)
    return "ok", 200

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=10000)
