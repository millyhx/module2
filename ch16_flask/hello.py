###########
#TASK 1
###########

from flask import Flask, render_template
app = Flask("MyApp")

@app.route("/")
def hello():
    return "Hello World"

#FIRST WE ARE IMPORTING THE MODULE WE NEED FROM PYTHON LIBRARIES
#WE ARE THEN NAMING OUR APP
#AFTERWARDS WE USE SOMETHING CALLED A DECORATOR WHICH TELLS THE
#SERVER TO DO SOMETHING INTERNALLY FOR US.
#WE THEN CREATE A FUNCTION CALLED HELLO WHICH WILL RETURN THE STRING
#"HELLO WORLD"

###########
#TASK 3
###########
    
@app.route("/<name>")
def hello_someone(name):
    return render_template("hello.html", name=name.title())

app.run(debug=True)

#WE THEN CREATE ANOTHER ROUTE WHICH WILL LEAD TO AN EMPTY VARIABLE
#AFTERWARDS ANOTHER FUNCTION IS CREATED WHICH HAS A VARIABLE AS THE PARAMETER. 
#CALLD NAME. 
#THEN WE RENDER THE TEMPLATE FROM HELLO.HTML
#WHATEVER IS TYPED AFTER THE BACKSLASH WILL BE RENDERED ACCORDING TO THE
#HTML FILE. WITHIN THAT FILE IS A TEMPLATE ON HOW TO DISPLAY CERTAIN THINGS.


#APP.RUN IS MAKING SURE THAT FLASK IS RUNNING YOUR APP.
