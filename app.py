import os
from flask import Flask, render_template

app = Flask(__name__)

file_list = [
    1, 2, 3, 4, 5
]


@app.route("/")
def helloWorld():
    return render_template("page_two.html", fileList=file_list)


if __name__ == "__main__":
    app.run(debug=True)
