from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    app_name = "Teli-Tracker"
    return render_template("index.html", name=app_name)

@app.route('/vendors.html')
def vendors():
    return render_template("vendors.html")

if __name__ == "__main__":
    app.run(debug=True)