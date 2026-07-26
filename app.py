from flask import Flask, jsonify, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = "super_secret_key_for_quiz"  # Required for session management

# Expanded list of AI Questions (15 Questions)
QUIZ_DATA = [
    {
        "id": 1,
        "question": "1. What does 'AI' stand for?",
        "options": [
            "Automated Intelligence",
            "Artificial Intelligence",
            "Advanced Intelligence",
            "Apple Intelligence",
        ],
        "answer": "Artificial Intelligence",
    },
    {
        "id": 2,
        "question": "2. Who is known as the 'Father of Artificial Intelligence'?",
        "options": [
            "Alan Turing",
            "Charles Babbage",
            "John McCarthy",
            "Elon Musk",
        ],
        "answer": "John McCarthy",
    },
    {
        "id": 3,
        "question": "3. Which programming language is most popular for AI development?",
        "options": ["Python", "Java", "C++", "HTML"],
        "answer": "Python",
    },
    {
        "id": 4,
        "question": "4. What is the full form of 'GPT' in ChatGPT?",
        "options": [
            "General Process Technology",
            "Generative Pre-trained Transformer",
            "Global Program Transfer",
            "General Purpose Text",
        ],
        "answer": "Generative Pre-trained Transformer",
    },
    {
        "id": 5,
        "question": "5. Which company developed ChatGPT?",
        "options": ["Google", "Microsoft", "OpenAI", "Meta"],
        "answer": "OpenAI",
    },
    {
        "id": 6,
        "question": "6. Which test is used to determine if a machine can think like a human?",
        "options": [
            "Turing Test",
            "IQ Test",
            "Voight-Kampff Test",
            "Unit Test",
        ],
        "answer": "Turing Test",
    },
    {
        "id": 7,
        "question": "7. What is the name of Google's flagship AI model?",
        "options": ["Gemini", "Alexa", "Siri", "Watson"],
        "answer": "Gemini",
    },
    {
        "id": 8,
        "question": "8. Which branch of AI allows machines to learn automatically from data?",
        "options": [
            "Machine Learning",
            "Web Development",
            "Database Management",
            "Cyber Security",
        ],
        "answer": "Machine Learning",
    },
    {
        "id": 9,
        "question": "9. What technology allows self-driving cars to 'see' their surroundings?",
        "options": [
            "Computer Vision",
            "Natural Language Processing",
            "Blockchain",
            "Cloud Computing",
        ],
        "answer": "Computer Vision",
    },
    {
        "id": 10,
        "question": "10. What does 'NLP' stand for in Artificial Intelligence?",
        "options": [
            "Natural Language Processing",
            "Neural Language Program",
            "Network Protocol Logic",
            "New Learning Process",
        ],
        "answer": "Natural Language Processing",
    },
    {
        "id": 11,
        "question": "11. Which AI concept is modeled after the human brain structure?",
        "options": [
            "Artificial Neural Networks",
            "Decision Trees",
            "Linear Regression",
            "Binary Search",
        ],
        "answer": "Artificial Neural Networks",
    },
    {
        "id": 12,
        "question": "12. What type of AI is designed to perform a single specific task?",
        "options": ["Narrow AI", "General AI", "Super AI", "Strong AI"],
        "answer": "Narrow AI",
    },
    {
        "id": 13,
        "question": "13. Which famous AI beat world chess champion Garry Kasparov in 1997?",
        "options": ["Deep Blue", "AlphaGo", "Watson", "ChatGPT"],
        "answer": "Deep Blue",
    },
    {
        "id": 14,
        "question": "14. Which company developed AlphaGo, the AI that beat a champion Go player?",
        "options": ["DeepMind (Google)", "IBM", "Tesla", "Amazon"],
        "answer": "DeepMind (Google)",
    },
    {
        "id": 15,
        "question": "15. What is the main goal of 'Generative AI'?",
        "options": [
            "To create new content (images, text, audio)",
            "To delete database entries",
            "To speed up internet connection",
            "To repair computer hardware",
        ],
        "answer": "To create new content (images, text, audio)",
    },
]


# 1. Login Page Route
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Simple validation
        if username and password:
            session["user"] = username
            return redirect(url_for("home"))
        else:
            return render_template(
                "login.html", error="Please fill in all fields!"
            )

    return render_template("login.html")


# 2. Quiz Home Route
@app.route("/")
def home():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("index.html", user=session["user"])


# 3. Logout Route
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))


# 4. Questions API Endpoint
@app.route("/api/questions", methods=["GET"])
def get_questions():
    if "user" not in session:
        return jsonify({"error": "Unauthorized"}), 401
    return jsonify(QUIZ_DATA)


if __name__ == "__main__":
    app.run(debug=True)