
# app.py - Backend Flask për TechBot nga MBPristina

from flask import Flask, request, jsonify
import openai
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Lejon kërkesat nga frontend-i në web

# Merr çelësin API nga variablat e ambientit për siguri
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    prompt = data.get("message")

    # Kufizo botin vetëm për pyetje teknologjike
    system_message = {
        "role": "system",
        "content": (
            "Ti je TechBot, një asistent që përgjigjet vetëm për teknologji, IT, rrjete, programim, siguri kibernetike dhe elektronikë. "
            "Mos u përgjigj nëse pyetja nuk ka lidhje me teknologjinë."
        )
    }

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                system_message,
                {"role": "user", "content": prompt}
            ]
        )

        reply = response.choices[0].message["content"]
        return jsonify({"response": reply})

    except Exception as e:
        return jsonify({"response": f"Gabim gjatë përgjigjes: {str(e)}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
