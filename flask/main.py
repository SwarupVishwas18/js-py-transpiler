from distutils.log import debug
from fileinput import filename
from flask import *
from converter import js_to_python, indentToNbsp

app = Flask(__name__, template_folder="template")


@app.route("/", methods=["POST", "GET"])
def main():
    if request.method == "POST":
        f = request.files["js-file"]
        f.save(f.filename)
        js_path = f.filename
        with open(js_path) as f:
            js_code = f.read()
        python_code = js_to_python(js_code)
        js = js_code.split("\n")
        python_code = indentToNbsp(python_code)
        py = python_code.split("\n")
        print(py)
        return render_template("index.html", js=js, py=py)
    return render_template("index.html")


@app.route("/comment", methods=["POST", "GET"])
def comment():
    if request.method == "POST":
        f = request.files["js-file"]
        f.save(f.filename)
        js_path = f.filename
        with open(js_path) as f:
            js_code = f.read()
        python_code = js_to_python(js_code)
        js = js_code.split("\n")
        python_code = indentToNbsp(python_code)
        py = python_code.split("\n")
        print(py)
        return render_template("comment.html", js=js, py=py)
    return render_template("comment.html")


@app.route("/codeindex", methods=["POST", "GET"])
def codeindex():
    if request.method == "POST":
        f = request.files["js-file"]
        f.save(f.filename)
        js_path = f.filename
        with open(js_path) as f:
            js_code = f.read()
        python_code = js_to_python(js_code)
        js = js_code.split("\n")
        python_code = indentToNbsp(python_code)
        py = python_code.split("\n")
        print(py)
        return render_template("codeindex.html", js=js, py=py)
    return render_template("codeindex.html")


if __name__ == "__main__":
    app.run(debug=True)
