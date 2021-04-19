# Entry poitn of application.


from flask import Flask



#Instancio con el nomrbe de la apliacipón. 
app = Flask(__name__)



# Para que no vaya en circuls y darle independencia a lso modulos en init se importará nuevamente
# routes.

from app import routes


