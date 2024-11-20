from flask import Flask, request, jsonify
from app.AccountRegistry import AccountRegistry
from app.PersonalAccount import PersonalAccount

app = Flask(__name__)

@app.route("/api/accounts", methods=['POST'])
def create_account():
   data = request.get_json()
   print(f"Create account request: {data}")
   konto = PersonalAccount(data["name"], data["surname"], data["pesel"])
   AccountRegistry.add_account(konto)
   return jsonify({"message": "Account created"}), 201

@app.route("/api/accounts/<pesel>", methods=['GET'])
def get_account_by_pesel(pesel):
    #implementacja powinna znaleźć się tutaj i powinna zwracać dane konta
    return jsonify({"imie": "imie"}), 200

@app.route("/api/accounts/<pesel>", methods=['PATCH'])
def update_account(pesel):
    #implementacja powinna znaleźć się tutaj
    return jsonify({"message": "Account updated"}), 200

@app.route("/api/accounts/<pesel>", methods=['DELETE'])
def delete_account(pesel):
    #implementacja powinna znaleźć się tutaj
    return jsonify({"message": "Account deleted"}), 200

if __name__ == "__main__":
    app.run(port=5003) 