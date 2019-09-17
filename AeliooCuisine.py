from flask import Flask, jsonify, request, redirect, render_template, g, url_for, send_file
from flask_cors import CORS
import sqlite3
import json

app = Flask(__name__)
CORS(app)


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def connect_db():
    sql = sqlite3.connect('aeliooo.s3db')
    # sqlite3.Row avoir un dict plutot qu'un tuple pour une ligne
    sql.row_factory = dict_factory
    return sql


def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


def addCommande(nom, adresse):
    #    Le client passe une commandes :
    # Requête POST @/commandes
    # JSON {'nom':'aaazaz','adresse' :'Rue azaz','etat':{....}}
    # Réponse JSON {'retour' :’OK’}
    db = get_db()
    req = f"insert into commandes(nom, adresse) values('{nom}','{adresse}')"
    db.execute(req)
    db.commit()

# (Enum des états des commandes :)
# (1 :Nouveau, 2 :En cours de préparation, 3 :Prêt, 4 :En cours de livraison, 5 :Livré)


@app.route('/commandes', methods=['POST', 'GET', 'PUT'])
def commandesClient():
    #   Le client récupère ses commandes :
    #   Requête GET @/commandes ?nomClient=Baratoux
    if request.method == 'GET':
        nomClient = request.args.get('nomClient')
        if nomClient != None:
            dico = {'commandes': [
                {'id': 1, 'nom': 'Gerard', 'etat': 1, 'adresse': 'rue Perpignan'}]}
    #   Réponse JSON {'commandes':[{'id':12,'etat':4 & 5},...]}
            return jsonify({'commandes': [{'id': jean, 'etat': 4}]})
        else:
            return '<h1>Nom, Adresse SVP !?</h1>'
    elif request.method == 'POST':
        dataJson = json.loads(request.data)
        # addCommande(recup['nom'], recup['adresse'])
        nomp = dataJson['nom']
        adressep = dataJson['adresse']
        req = f"insert into commandes(nom, adresse, etat) values('{nomp}','{adressep}','{1}')"
        db = get_db()
        db.execute(req)
        db.commit()

        return jsonify({'status': 'ok'})

    else:
        recup = request.get_json()  # put
        print("OK", recup)
        return 'ok'


@app.route('/cuisine', methods=['GET'])
def addCommande():
    #     La cuisine récupère ses commandes (Qt, Ui_Mainwindow)  etat: 1:
    #     Requête GET @/commandes/cuisine
    if request.method == 'GET':
        dico = {'commandes': [
            {'id': 1, 'nom': 'Gerard', 'etat': 1, 'adresse': 'rue Perpignan'}]}
        return jsonify(dico)


@app.route('/newDetection', methods=['POST'])
def newDetection():
    print("reception")

    recup = request.get_json()
    dataJson = json.loads(recup)
    print(dataJson)

    datetime = (dataJson['datetime'])
    plaque = (dataJson['plaque'])
    image = (dataJson['image'])

    db = get_db()
    db.execute('insert into champs (datetime, plaque,image) values (?,?,?)', [
               datetime, plaque, image])
    db.commit()

    return ""


#   La cuisine met la commande à jour ... click sur 1 nouvelle commande
#   & click commande en cours:
# Requête PUT @/commandes
# Réponse JSON {'id':12,'etat':2 & 3}

# La livreur met la commande à jour ... en cours de livraison & livré:
# Requête PUT @/commandes
# Réponse JSON {'id':12,'etat':4 & 5}
if __name__ == "__main__":
    app.run(debug=True)
