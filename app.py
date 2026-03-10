from flask import Flask, render_template, request, jsonify
from chatbot.nlp_engine import process_query

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_msg = request.form["message"]
    bot_response = process_query(user_msg)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)

