from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "dein_geheimer_schluessel_hier" # Direkt nach app = Flask(__name__) hinzufügen

@app.route("/")
def startseite():
    if "charakter" in session:
        return render_template("index.html", char=session["charakter"])
    return redirect("/erstellen")

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
        session["charakter"] = {
            "name": request.form["name"],
            "klasse": request.form["klasse"],
            "level": 1,
            "hp": 100,
            "gold": 500,
        }
        return redirect(f"/profil")
    return render_template("erstellen.html")

@app.route("/profil")
def profil_session():
    if "charakter" in session:
        return render_template("profil.html", char=session["charakter"])
    return redirect("/erstellen")

if __name__ == "__main__":
    app.run(debug=True)