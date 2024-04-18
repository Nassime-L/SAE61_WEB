from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

#infos DB
app.config['MYSQL_HOST'] = '172.19.0.3'
app.config['MYSQL_USER'] = 'sae61'
app.config['MYSQL_PASSWORD'] = 'sae61'
app.config['MYSQL_DB'] = 'sae61'

mysql = MySQL(app)

@app.route("/")
def accueil():
    return render_template('accueil.html')

@app.route("/inscription", methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		Users = request.form
		Nom = Users['nom']
		Prenom = Users['prenom']
		identifiant = Users['identifiant']
		mail = Users['email']
		password = Users['mdp']
		hashed = generate_password_hash(password)
		cur = mysql.connection.cursor()
		cur.execute("INSERT INTO Utilisateurs(Nom, Prenom, identifiant, mail, password) VALUES (%s,%s,%s,%s,%s)",(Nom, Prenom, identifiant, mail, hashed))
		mysql.connection.commit()
		cur.close()
		return "Vous êtes inscrit !"
	return render_template('inscription.html')

"""@app.route("/connexion" methods=['GET', 'POST'])
def connexion():
	if request.method == 'POST':
	
    return render_template('connexion.html')///"""


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
