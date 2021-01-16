from flask import Flask, render_template, request, redirect
import speech_recognition as sr

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    transcript = ""
    if request.method == "POST":
        print("FORM DATA RECEIVED")
        # Checks to see if the file is what was requested
        if "file" not in request.files:
            return redirect(request.url)
        # If no file was uploaded, redirect
        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)
        # Pass the file into the recognizer object and read it
        if file:
            recognizer = sr.Recognizer()
            audioFile = sr.AudioFile(file)
            with audioFile as source:
                data = recognizer.record(source)
            transcript = recognizer.recognize_google(data, key=None)

    return render_template("index.html", transcript=transcript)


if __name__ == "__main__":
    app.run(debug=True, threaded=True)
