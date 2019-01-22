import requests 
import random

from flask import Flask, render_template
app = Flask("MyApp")
@app.route("/")
def create_fairytale():

    ################
    #name and gender
    ################
    
    endpoint = "https://uinames.com/api/?region=england"
    payload = {"name": [0]}
    
    response = requests.get(endpoint, params=payload)
    data = response.json()
    
    name = data["name"]
    gender = data["gender"]
    
    
    if gender == "female":
        print("Once upon a time, there was a girl called {}.".format(name))
    if gender == "male":
        print("Once upon a time, there was a boy called {}.".format(name))
    
    
    if gender == "female":
        pronoun = "she"
    if gender == "male":
        pronoun = "he"
    
    ################
    #postcode
    ################
    
    endpoint = "https://api.postcodes.io/random/postcodes"
    payload = {"result":"postcode"}
    
    response = requests.get(endpoint, params=payload)
    data2 = response.json()
    
    if response.status_code == 200:
            latitude = data2['result']['latitude']
            longitude = data2['result']['longitude']
            district = data2["result"]["admin_district"]
    
    

            
    ################
    #weather
    ################
    
    
    api_key = "bb281b413a6c7b085bffadb8ccd9e12d"
    endpoint =  "https://api.darksky.net/forecast/"
    payload = (api_key + "/" + str(latitude) +"," + str(longitude))
    url = endpoint +payload
    
    response = requests.get(url)
    data3 = response.json()
 
    weather = data3["currently"]["summary"]
   
    print("{} lived in a place called {} where the weather was always {}.".format(name,district,weather))

    
    
    ################
    #age
    ################
    
    for x in range(10):
        age = random.randint(5,10)
        
    
    print("{} was the youngest in".format(name), pronoun,"family, as", pronoun, "was only", age)
    print(pronoun.title(), "always wished that", pronoun, "could own a pet. However, {}'s family always said no because".format(name), pronoun, "was too young.")
    
    

    ################
    #suspense
    ################
    endpoint = "https://uinames.com/api/?region=england"
    payload = {"name": [0]}
    
    response = requests.get(endpoint, params=payload)
    data4 = response.json()
    
    pet_name = data4["name"]
    
    print("SUDDENLY... {} stumbled across something. It was a...".format(name))
    
    

    
    ################
    #pet
    ################
    
    pets = ["dog", "cat", "llama", "skunk", "meerkat", "zebra", "cheetah", "hippo", "gerbil", "camel", "mouse"]
    
    for i in data:
        pet_type = (random.choice(pets))
    
    
    print(pet_type)
    print("{} was so excited!".format(name), pronoun.title(), "decided to call it...", pet_name.upper())
        
        
    return render_template("fairytale_template.html", name = data["name"], gender = data["gender"], latitude = data2['result']['latitude'], longitude = data2['result']['longitude'], district = data2["result"]["admin_district"], weather = data3["currently"]["summary"], age = random.randint(5,10), pet_name = data4["name"], pets = ["dog", "cat", "llama", "skunk", "meerkat", "zebra", "cheetah", "hippo", "gerbil", "camel", "mouse"], pet_type = (random.choice(pets)), pronoun = (("he") or ("she")))
    
app.run(debug=True)
create_fairytale()


#https://uinames.com/
#https://postcodes.io/
#https://darksky.net/dev/account