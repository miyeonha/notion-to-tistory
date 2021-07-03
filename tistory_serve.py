from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def convert_notion():

    return render_template('tistory_index.html')

if __name__ == "__main__":
    app.run(debug=True, threaded=True)