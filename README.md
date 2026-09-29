# AI Student Study Assistant

## Description

AI Student Study Assistant is a small web application designed to
help students understand academic concepts using an AI model.

A student enters a question into the web interface. The application
sends the question to an AI service and displays the generated
explanation.

## Features

- Ask academic questions
- Receive AI-generated explanations
- Simple web interface
- Designed for student learning
- Can be extended with quizzes and study-plan generation

## Technologies

- Python
- Flask
- HTML
- CSS
- OpenAI API

## How It Works

1. The student enters a question.
2. The HTML form sends the question to the Flask application.
3. Flask sends the question to the AI API.
4. The AI generates a response.
5. Flask sends the response back to the webpage.

## Security

The API key is stored as an environment variable and is not included
in the source code.

## Future Improvements

- Generate quizzes
- Generate personalized study plans
- Add conversation history
- Add user accounts
- Add answer-quality checks
