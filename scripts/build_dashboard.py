# -*- coding: utf-8 -*-
"""Génère la page tableau de bord à partir des mêmes données que le registre."""
import json, sys
import os; ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_registre import ITEMS, DATE_VUE

rows = []
for i, it in enumerate(ITEMS, start=1):
    cat, titre, det, src, typ, pays, dv, est, prix, statut, url = it
    rows.append({"id": f"B{i:04d}", "vu": DATE_VUE, "cat": cat, "titre": titre, "det": det, "src": src,
                 "typ": typ, "pays": pays, "date": dv, "est": est, "prix": prix, "statut": statut, "url": url,
                 "nouveau": False})

JOURNAL = [
    {"date": "2026-08-25", "type": "État des lieux initial", "ajout": 72, "brief": "Brief n°0",
     "note": "Balayage complet — 4 explorateurs, ~500 requêtes. Sources bloquées aux robots : Interencheres, Drouot, eBay, Leboncoin, Catawiki, Delcampe, Cairn, HAL, Gazette Drouot, Tribune de l'Art."}
]

ALERTES = [
    ("Interencheres", "Alerte mot-clé « Bellangé »", "indispensable"),
    ("Drouot.com", "Alerte « Bellangé »", "indispensable"),
    ("eBay.fr", "Recherche sauvegardée « Bellangé » + alerte", "indispensable"),
    ("Leboncoin", "Alerte « bellangé »", "utile"),
    ("Catawiki", "Alerte « Bellangé »", "utile"),
    ("Delcampe", "Alerte « Bellangé »", "utile"),
    ("Invaluable", "Alerte mot-clé « Bellangé »", "utile"),
    ("Proantic", "Alerte « Bellangé »", "utile"),
    ("Google Alerts", "« Hippolyte Bellangé » (hebdo)", "utile"),
    ("Google Scholar", "Alerte « Hippolyte Bellangé »", "utile"),
    ("Gazette Drouot", "Newsletter", "optionnel"),
    ("MutualArt", "Suivre l'artiste (gratuit)", "optionnel"),
]

data_json = json.dumps(rows, ensure_ascii=False)
journal_json = json.dumps(JOURNAL, ensure_ascii=False)
alertes_json = json.dumps(ALERTES, ensure_ascii=False)

html = open(os.path.join(ROOT,"dashboard","template.html"),encoding="utf-8").read()
html = html.replace("__DATA__", data_json).replace("__JOURNAL__", journal_json).replace("__ALERTES__", alertes_json)
page = ("<!doctype html>\n<html lang=\"fr\">\n<head>\n<meta charset=\"utf-8\">\n<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">\n" + html.split("<style>")[0] + "<style>" + html.split("<style>",1)[1].split("</style>")[0] + "</style>\n</head>\n<body>\n" + html.split("</style>",1)[1] + "\n</body>\n</html>\n")
with open(os.path.join(ROOT,"dashboard","index.html"), "w", encoding="utf-8") as f:
    f.write(page)
with open(os.path.join(ROOT,"dashboard","artifact.html"), "w", encoding="utf-8") as f:
    f.write(html)
print("ok", len(html))
