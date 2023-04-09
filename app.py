import os
from flask import request
from flask import Flask
from flask import render_template

app = Flask(__name__)
UPLOAD_FOLDER = "D:\Academics\Detection\static"

@app.route('/')
def upload_predict():
    if request.method == "POST":
        image_file = request.files["image"]
        if image_file:
            image_location = os.path.join(
                UPLOAD_FOLDER,
                image_file.filename
            )
            image_file.save(image_location)
            #pred = predict(image_location, MODEL)
            return render_template("index.html",prediction = 1)
    return render_template("index.html", prediction = 0)

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == "__main__":
    app.run(port=12000,debug=True)
