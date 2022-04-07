from flask import Flask, render_template, request

app = Flask(__name__)

"""
@app.route("/post", methods=['POST'])
"""

@app.route("/")
def homepage():
    return render_template("index.html")


@app.route("/quemsomos")
def quemsomos():
    return render_template("quemsomos.html")


if __name__ == "__main__":
    app.run(debug=True)