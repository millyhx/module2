from flask import Flask, render_template, request
app = Flask("FormApp")

#HERE WE ARE IMPORTING THE MODULES WE NEED FROM THE PYTHON LIBRARIES
#THEN WE ARE NAMING THE FLASK APP THAT WE WANT TO CREATE

###########
#TASK 5
###########

@app.route("/about")
def about():
    return render_template("about.html", title="about")

#HERE WE HAVE CREATED A ROUTE THAT WILL LEAD TO AN ABOUT PAGE
#AND WE HAVE RENDERED A TEMPLATE AS THE RETURN THAT LINKS TO 
#AN HTML FILE CALLED ABOUT. 

###########
#TASK 5
###########
    
@app.route("/confirmation", methods=["POST"])
def confirmation():
    form_data = request.form
    email = form_data["email"]
    result="ALL OK"
    return render_template("confirmation.html", title="Form confirmation", **locals())

app.run(debug=True)

#WE THEN CREATE ANOTHER ROUTE CALLED CONFIRMATION.
#WITHIN THIS ROUTE WE CREATE A FUNCTION CALLED CONFIRMATION
#A VARIABLE IS CREATED CALLED FORM_DATA THAT LINKS TO SOMETING THAT
#WILL REQUEST FOR THE FORM.
#THEN WE CREATE ANOTHER VARIABLE CALLED EMAIL THAT LINKS TO THE FORM DATA
#AND SPECIFICALLY LOOKS AT THE EMAIL KEY. 
#ANOTHER VAIRABLE IS CREATED WHICH IS GIVEN A STRING VALUE
#WE THEN RENDER THE TEMPLATE TO CONFIRMATION.HTML