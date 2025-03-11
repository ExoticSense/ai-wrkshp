import os
from google import genai
from dotenv import load_dotenv
from flask import Flask,jsonify,request
app = Flask(__name__)
load_dotenv()
api_key = os.getenv("API_KEY")

client = genai.Client(api_key = api_key)

# response = client.models.generate_content(
#     model="gemini-2.0-flash",
#     contents = "hi how are u my dear sexy gemini"
# )

@app.route("/home", methods = ["GET"])
def home():
    return "hello world"
@app.route('/chat', methods = ['POST'])
def chat():
    try:
        data = request.get_json()
        if 'prompt' not in data:
            return jsonify({
                "error": "Prompt not found in data"
            })
        prompt = data['prompt']
        response = client.models.generate_content(
            model="gemini-2.0-flash", 
            contents = prompt
        )
        return jsonify({
            "ai_response": response.text
        }) ,200
    except Exception as e:
        return jsonify({
            "error":str(e)
        }), 500
if (__name__) == '__main__':
    app.run(debug = True)
# print(response.text)