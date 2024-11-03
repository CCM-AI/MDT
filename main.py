from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample responses for common questions
responses = {
    "What is your name?": "I am the AI assistant for the MDT team.",
    "What is the role of the MDT?": "The MDT team collaborates to provide comprehensive patient care.",
    "How can I contact a doctor?": "You can reach out to your doctor via the patient portal or contact the clinic directly.",
    "What should I do if I have a medical emergency?": "Please call emergency services or go to the nearest emergency room immediately."
}

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get('question', '')
    answer = responses.get(question, "I'm sorry, I don't have an answer for that.")
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)
