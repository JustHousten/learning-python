from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///spiel.db'
app.config['SECRET_KEY'] = 'geheimer-schluessel'
db = SQLAlchemy(app)

class Charakter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    klasse = db.Column(db.String(20), nullable=False)
    level = db.Column(db.Integer, default=1)
    hp = db.Column(db.Integer, default=100)
    gold = db.Column(db.Integer, default=500)

with app.app_context():
    db.create_all()
    print("Datenbank und Tabelle wurden erstellt.")

@app.route('/')
def startseite():
    charaktere = Charakter.query.all()
    return render_template('index.html', charaktere=charaktere)

@app.route("/erstellen", methods=["GET", "POST"])
def erstellen():
    if request.method == "POST":
        neuer_char = Charakter(
            name=request.form["name"],
            klasse=request.form["klasse"]
        )
        db.session.add(neuer_char)
        db.session.commit()
        return redirect("/")
    return render_template("erstellen.html")

if __name__ == '__main__':
    app.run(debug=True)