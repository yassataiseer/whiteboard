from flask import Flask, render_template,request,session

app = Flask(__name__)


@app.route("/")
def main():
    return render_template ('home.html')


if __name__ == '__main__':
    app.run(port=5000, debug=True) 