
from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the trained spam detection model
with open("spam_model.pkl", "rb") as file:
    model = pickle.load(file)


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    email_text = ""

    if request.method == "POST":
        email_text = request.form.get("email", "").strip()

        if email_text:
            prediction = model.predict([email_text])[0]

            if prediction == "spam":
                result = "Spam"
            else:
                result = "Not Spam"

    return render_template(
        "index.html",
        result=result,
        email_text=email_text
    )


if __name__ == "__main__":
    app.run(debug=True)
