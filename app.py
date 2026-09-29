import os
from flask import Flask, request, render_template
from openai import OpenAI

app = Flask(__name__)

API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=API_KEY) if API_KEY else None

SYSTEM_PROMPT = (
    "You are a helpful student study assistant. "
    "Explain academic concepts in simple English, "
    "give examples, and create short practice questions "
    "when requested."
)


@app.route("/", methods=["GET", "POST"])
def home():

    answer = ""
    question = ""

    if request.method == "POST":

        question = request.form.get("question", "").strip()

        if not question:
            answer = "Please enter a question."

        elif client is None:
            answer = (
                "The AI service is not configured. "
                "Please set the OPENAI_API_KEY environment variable."
            )

        else:
            try:

                response = client.responses.create(
                    model="gpt-5-mini",
                    instructions=SYSTEM_PROMPT,
                    input=question
                )

                answer = response.output_text

            except Exception as error:

                answer = f"AI request failed: {error}"

    return render_template(
        "index.html",
        answer=answer,
        question=question
    )


if __name__ == "__main__":
    app.run(debug=True)
