from flask import Flask, render_template, request
import tensorflow as tf
import pickle

app = Flask(__name__)

# Model ve Vectorizer'ı yükleme
model = tf.keras.models.load_model("xss_detection_model.h5")

with open("vectorizer.pkl", "rb") as file:
    vectorizer = pickle.load(file)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        user_input = request.form["payload"]
        transformed_input = vectorizer.transform([user_input]).toarray()
        prediction = model.predict(transformed_input)

        if prediction[0] > 0.5:
            result = "Bu bir XSS payload!"
        else:
            result = "Bu bir XSS payload DEĞİL!"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
