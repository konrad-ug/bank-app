from flask import Flask, request, jsonify
from app.AccountRegistry import AccountRegistry
from app.PersonalAccount import PersonalAccount

app = Flask(__name__)


@app.route("/api/accounts", methods=['POST'])
def create_account():
    data = request.get_json()
    print(f"Create account request: {data}")
    if AccountRegistry.get_account_by_pesel(data["pesel"]) is not None:
        return jsonify({"message": "Konto z takim pesel juz istnieje"}), 409
    konto = PersonalAccount(data["name"], data["surname"], data["pesel"])
    AccountRegistry.add_account(konto)
    return jsonify({"message": "Account created"}), 201


@app.route("/api/accounts/<pesel>", methods=['GET'])
def get_account_by_pesel(pesel):
    account = AccountRegistry.get_account_by_pesel(pesel)
    if account is None:
        return jsonify({"message": "konta brak"}), 404
    return jsonify({
        "name": account.imie,
        "surname": account.nazwisko,
        "saldo": account.saldo
    }), 200


@app.route("/api/accounts/<pesel>", methods=['PATCH'])
def update_account(pesel):
    #implementacja powinna znaleźć się tutaj
    return jsonify({"message": "Account updated"}), 200


@app.route("/api/accounts/<pesel>", methods=['DELETE'])
def delete_account(pesel):
    account = AccountRegistry.get_account_by_pesel(pesel)
    if account is not None:
        AccountRegistry.accounts.remove(account)
        return jsonify({"message": "Account deleted"}), 200
    return jsonify({"message": "account not found"}), 404


# @app.route("/api/accounts/<pesel>/transfer", methods=['POST'])
# def transfer(pesel):
#     data = request.get_json()
#     account = AccountRegistry.get_account_by_pesel(pesel)
#     if account is None:
#         return jsonify({"message": "Account not found"}), 404
#     if data["type"] == "outgoing":
#         result = account.outgoing_transfer(data["amount"])
#     if data["type"] == "incoming":
#         result = account.incoming_transfer(data["amount"])
#     if data["type"] == "express":
#         result = account.outgoing_express_transfer(data["amount"])
#     if result:
#         return jsonify({"message": "Transfer completed"}), 200
#     return jsonify({"message": "Transfer failed"}), 422


@app.route("/api/accounts/<pesel>/transfer", methods=['POST'])
def transfer(pesel):
    data = request.get_json()
    account = AccountRegistry.get_account_by_pesel(pesel)
    if account is None:
        return jsonify({"message": "Account not found"}), 404

    def handle_outgoing():
        result = account.outgoing_transfer(data["amount"])
        if result:
            return jsonify({"message": "Outgoing transfer processed"}), 200
        else:
            return jsonify({"message": "Transfer failed"}), 422

    def handle_incoming():
        result = account.incoming_transfer(data["amount"])
        if result:
            return jsonify({"message": "Incoming transfer processed"}), 200
        else:
            return jsonify({"message": "Transfer failed"}), 422

    def handle_express():
        result = account.outgoing_express_transfer(data["amount"])
        if result:
            return jsonify({"message": "Outgoing transfer processed"}), 200
        else:
            return jsonify({"message": "Transfer failed"}), 422

    def handle_default():
        return jsonify({"message": "Unknown transfer type"}), 422

    switch = {
        "outgoing": handle_outgoing,
        "incoming": handle_incoming,
        "express": handle_express
    }

    result = switch.get(data["type"], handle_default)()
    return result
