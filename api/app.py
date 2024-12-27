from flask import Flask, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

genai.configure(api_key="AIzaSyBjFl5pgfdrM59pZwUiafIbS3XQoAn67bM")
model = genai.GenerativeModel("gemini-1.5-flash")

@app.route("/api/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    bot_response = model.generate_content(user_message).text
    return jsonify({"response": bot_response})

# Export the app for Vercel
app = app
