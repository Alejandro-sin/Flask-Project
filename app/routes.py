'''

Si quiero construir un hombrepage es mejor usar los tempaltes y apra eso imrota
las funciones de render_tempalte

'''





from app import app
from flask import render_tempalte

@app.route("/")
@app.route("/index")
def index():
    return render_tempalte("index.html")

