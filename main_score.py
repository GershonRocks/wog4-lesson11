from flask import Flask, render_template
from utils import BAD_RETURN_CODE
from score import load_score_file
app = Flask(__name__)


@app.route("/score_server")
def score_server():
    score_file_result = load_score_file()
    if score_file_result != 0:
        return render_template("score.html", score=score_file_result), 200
    else:
        error = "Wrong score value"
        return render_template("error.html", error=error), BAD_RETURN_CODE


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=30000)
