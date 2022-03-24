from balance import app

@app.route("/")
def inicio():
    return "Working as intended"