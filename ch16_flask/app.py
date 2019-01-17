from flask import Flask, render_template, request
app = Flask("FormApp")

@app.route("/about")
def about():
    return render_template("about.html", title="about")

@app.route("/confirmation", methods=["POST"])
def confirmation():
    form_data = request.form
    email = form_data["email"]
    result="ALL OK"
    return render_template("confirmation.html", title="Form confirmation", **locals())

app.run(debug=True)
