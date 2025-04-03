from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

# JSON fájl betöltése
with open("cikklista_apihoz.json", "r", encoding="utf-8") as f:
    adatbazis = json.load(f)["cikkek"]

@app.route("/cikk", methods=["GET"])
def cikk_kereses():
    keresett = request.args.get("q", "").lower()
    talalatok = [
        cikk for cikk in adatbazis
        if keresett in cikk["cikkszam"].lower() or keresett in cikk["nev"].lower()
    ]
    return jsonify({"talalatok": talalatok})

if __name__ == "__main__":
    app.run(debug=True)
