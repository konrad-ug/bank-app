from flask import Flask, request, jsonify
from app.RejestrKont import RejestrKont
from app.Konto import Konto

app = Flask(__name__)

@app.route("/konta/stworz_konto", methods=['POST'])
def stworz_konto():
    dane = request.get_json()
    print(f"Request o stworzenie konta z danymi: {dane}")
    if RejestrKont.wyszukaj_konto_z_peselem(dane["pesel"]) != None:
        return jsonify("Konto z podanym peselem juz istnieje"), 400
    konto = Konto(dane["imie"], dane["nazwisko"], dane["pesel"])
    RejestrKont.dodaj_konto(konto)
    return jsonify("Konto stworzone"), 201

@app.route("/konta/konto/<pesel>", methods=['PUT'])
def aktualizuj_konto(pesel):
    dane = request.get_json()
    print(f"Request o update konta z danymi: {dane}")
    konto = RejestrKont.wyszukaj_konto_z_peselem(pesel)
    print("konto znalezione")
    konto.imie = dane["imie"] if "imie" in dane else konto.imie
    konto.nazwisko = dane["nazwisko"] if "nazwisko" in dane else konto.nazwisko
    konto.pesel = dane["pesel"] if "pesel" in dane else konto.pesel
    konto.saldo = dane["saldo"] if "saldo" in dane else konto.saldo
    return jsonify("Update zakończony powodzeniem"), 200

@app.route("/konta/ile_kont", methods=['GET'])
def ile_kont():
    return {"ilosc_kont_w_rejestrze":RejestrKont.ile_kont()},200

@app.route("/konta/konto/<pesel>", methods=['GET'])
def wyszukaj_konto_z_peselem(pesel):
    print(f"Request o konto z peselem: {pesel}")
    konto = RejestrKont.wyszukaj_konto_z_peselem(pesel)
    print(konto)
    if (konto == None):
        return {"komunikat":"Konto nie zostało znalezione"}, 404
    return {"imie":konto.imie, "nazwisko":konto.nazwisko,"saldo":konto.saldo}, 200

@app.route("/konta/konto/<pesel>", methods=['DELETE'])
def usun_konto_z_peselem(pesel):
    print(f"Request o usuniecie z peselem: {pesel}")
    RejestrKont.usun_konto_z_peselem(pesel)
    return {"komunikat":"konto usuniete"}, 202

@app.route("/konta/wyczysc", methods=['DELETE'])
def wyczysc_rejestr():
    print(f"Request o usuniecie wszystkich kont")
    RejestrKont.wyczysc_rejestr()
    return {"komunikat":"Rejest wyczyszczony"}, 202