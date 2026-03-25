from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Context (simple global for demo)
context = {
    "last_intent": None,
    "order_id": None
}

def detect_intent(user_input):
    user_input = user_input.lower()

    if "hi" in user_input or "hello" in user_input:
        return "greeting"
    elif "order" in user_input:
        return "order_status"
    elif "issue" in user_input or "problem" in user_input:
        return "complaint"
    elif "bye" in user_input:
        return "goodbye"
    elif user_input.isdigit():
        return "provide_order_id"
    else:
        return "unknown"

def get_response(user_input):
    intent = detect_intent(user_input)

    if intent == "greeting":
        context["last_intent"] = "greeting"
        return "Hi! How can I assist you?"

    elif intent == "order_status":
        context["last_intent"] = "order_status"
        return "Please provide your order ID."

    elif intent == "provide_order_id":
        if context["last_intent"] == "order_status":
            context["order_id"] = user_input
            return f"Your order {user_input} is out for delivery."
        else:
            return "Please tell me how I can help you first."

    elif intent == "complaint":
        context["last_intent"] = "complaint"
        return "I'm sorry for the inconvenience. Please describe your issue."

    elif intent == "goodbye":
        return "Thank you! Have a great day."

    else:
        return "I didn't understand that. Can you rephrase?"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    response = get_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)