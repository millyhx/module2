from flask import Flask, render_template
app = Flask("MyApp")

@app.route("/")
def hello():
    return "Hello World"


@app.route("/about")
def hello_someone(name):
    return render_template("hello.html", name=name.title())

app.run(debug=True)


