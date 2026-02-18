from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def startseite():
    charakter = {
        "name": "Housten",
        "klasse": "Krieger",
        "level": 15,
        "hp": 3000,
        "gold": 48000 
    }
    return render_template("index.html", char=charakter)

@app.route("/profil/<name>")
def profil(name):
    charakter = {
        "name": name,
        "klasse": "Krieger",
        "level": 15,
        "hp": 3000,
        "gold": 48000 
    }
    return render_template("profil.html", char=charakter)

@app.route("/erstellen", methods=["GET", "POST"])
def erstellen():
    if request.method == "POST":
        name = request.form["name"]
        klasse = request.form["klasse"]
        return redirect(f"/profil/{name}")
    return render_template("erstellen.html")

if __name__ == "__main__":
    app.run(debug=True)