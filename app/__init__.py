# Entry poitn of application.


from flask import Flask



#Instancio con el nomrbe de la apliacipón. 
app = Flask(__name__)

# Creamos un rute para correr la aplciación7


@app.route("/")
@app.route("/index")
def index():
    return "<h1>Flask app</h1>"


