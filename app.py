
import joblib
import gradio as gr

# Load trained model and vectorizer
model = joblib.load("models/nigerian_language_model.pkl")
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")


def predict_language(text):
    if not text or not text.strip():
        return "Please enter a phrase.", 0.0, {}

    features = vectorizer.transform([text])

    probabilities = model.predict_proba(features)[0]
    classes = model.classes_

    results = {
        language: float(probability)
        for language, probability in zip(classes, probabilities)
    }

    prediction = model.predict(features)[0]
    confidence = max(probabilities)

    return prediction, confidence, results


demo = gr.Interface(
    fn=predict_language,
    inputs=gr.Textbox(
        label="Enter a phrase",
        placeholder="Type a phrase in English, Hausa, Igbo, or Yoruba..."
    ),
    outputs=[
        gr.Textbox(label="Predicted Language"),
        gr.Number(label="Confidence"),
        gr.Label(label="Language Probabilities")
    ],
    title="🇳🇬 Nigerian Language Identifier",
    description="Identify whether a short phrase is English, Hausa, Igbo, or Yoruba.",
    examples=[
        ["Bawo ni o se wa loni?"],
        ["Ina kwana? Ya ya gida?"],
        ["Kedu ka ị mere taa?"],
        ["How are you doing today?"]
    ]
)

demo.launch(share=True)
