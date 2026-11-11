#!/usr/bin/env python3
# Baut die statische Seite nach ./site (ESINT AT-Rechner)
import os, pathlib
BASE = "https://esint-dev.github.io/at-rechner/"
ABRUF = "11.11.2026"
STAND = "Mi, 11.11.2026"
KEY = open(".indexnow_key").read().strip()
OUT = pathlib.Path("site")

SRC = {
 "km_bmf": ("BMF – Kilometergeld", "https://www.bmf.gv.at/themen/steuern/kraftfahrzeuge/kilometergeld.html"),
 "km_oe": ("oesterreich.gv.at – Kilometergeld", "https://www.oesterreich.gv.at/de/themen/steuern_und_finanzen/unterstuetzungen_beihilfen_und_foerderungen/pendlerpauschale_und_kilometergeld/Seite.350300"),
 "ris26": ("RIS – § 26 Z 4 EStG 1988 (Fassung ab 17.10.2026)", "https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004570&Paragraf=26"),
 "usp_reise": ("USP – Reisekosten (Selbständige)", "https://www.usp.gv.at/themen/steuern-finanzen/steuerliche-gewinnermittlung/weitere-informationen-zur-steuerlichen-gewinnermittlung/betriebseinnahmen-und-ausgaben/reisekosten.html"),
 "usp_dienst": ("USP – Kosten bei Dienstreisen", "https://www.usp.gv.at/themen/mitarbeiter-und-gesundheit/entgelt/kosten-bei-dienstreisen.html"),
 "usp_ku": ("USP – Kleinunternehmerregelung ab 2025", "https://www.usp.gv.at/aktuelles/newsliste/kleinunternehmerregelung-ab-2025.html"),
 "wko_ku": ("WKO – Kleinunternehmerregelung (Umsatzsteuer)", "https://www.wko.at/steuern/kleinunternehmerregelung-umsatzsteuer"),
 "svs_neu": ("SVS – Informationen Neue Selbständige (PDF, Werte 2026)", "https://www.svs.at/cdscontent/load?contentid=10008.763401&version=1767089471"),
 "svs_beitr": ("SVS – Beiträge PV, KV, UV 2026 (PDF)", "https://www.svs.at/cdscontent/load?contentid=10008.763406&version=1768295866"),
 "svs_rechner": ("SVS – offizieller Beitragsrechner", "https://www.svs.at/"),
}
def src(*keys):
    items = "".join(f'<li><a href="{SRC[k][1]}" rel="noopener">{SRC[k][0]}</a> (abgerufen {ABRUF})</li>' for k in keys)
    return f'<h2>Quellen</h2><ul class="src">{items}</ul>'

AD = f'''<aside class="ad" aria-label="Werbung">
<p class="adlabel">Werbung (eigenes Produkt von ESINT)</p>
<p>Excel für Kleinunternehmer in Österreich: Einnahmen-Ausgaben-Rechnung, Prüfung der 55.000-€-Grenze, SVS- und Steuer-Rücklage, Rechnungsvorlage.</p>
<p><a class="btn" href="https://gumroad.com/l/hipixo" rel="sponsored noopener">Gratis-Lite herunterladen</a>
<a class="btn alt" href="https://gumroad.com/l/qxclfr" rel="sponsored noopener">Vollversion (19 €) ansehen</a></p>
<p class="small">Verkauf über Gumroad. Rechenhilfe, keine Steuerberatung.</p>
</aside>'''

DISCLAIMER = f'''<p class="disc"><strong>Unverbindlich:</strong> Diese Rechner sind eine einfache Rechenhilfe. Sie sind keine Steuer- oder Rechtsberatung und ersetzen keine Auskunft von Finanzamt, SVS, WKO oder Steuerberatung. Angaben ohne Gewähr, Stand {STAND}. Maßgeblich sind die verlinkten amtlichen Quellen. <a href="{BASE}impressum/">Impressum &amp; Haftung</a></p>'''

NAV = [("", "Übersicht"), ("kleinunternehmergrenze/", "Kleinunternehmergrenze"), ("kilometergeld/", "Kilometergeld"), ("diaeten-inland/", "Diäten Inland"), ("impressum/", "Impressum")]

def page(path, title, desc, body, h1, js=True):
    nav = " ".join(f'<a href="{BASE}{p}"{" aria-current=page" if p==path else ""}>{n}</a>' for p,n in NAV)
    url = BASE + path
    html = f'''<!doctype html>
<html lang="de-AT">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:type" content="website">
<link rel="stylesheet" href="{BASE}style.css">
</head>
<body>
<header><a class="brand" href="{BASE}">ESINT <span>AT-Rechner</span></a><nav>{nav}</nav></header>
<main>
<h1>{h1}</h1>
{body}
{DISCLAIMER}
</main>
<footer><p>© 2026 ESINT · <a href="https://github.com/esint-dev/at-rechner">Quellcode auf GitHub</a> · <a href="{BASE}impressum/">Impressum, Haftung, Datenschutz</a> · Stand {STAND}</p></footer>
{'<script src="'+BASE+'app.js" defer></script>' if js else ''}
</body>
</html>
'''
    d = OUT / path
    d.mkdir(parents=True, exist_ok=True)
    (d / "index.html").write_text(html, encoding="utf-8")

# --- Übersicht
page("", "Rechner für Selbständige in Österreich 2026 – Kleinunternehmergrenze, Kilometergeld, Diäten | ESINT",
 "Kostenlose Rechner für Selbständige in Österreich 2026: Kleinunternehmergrenze 55.000 € mit Toleranz, Kilometergeld und Tagesgeld/Nächtigungsgeld Inland – mit amtlichen Quellen.",
 f'''<p class="lead">Drei kostenlose Rechner für Selbständige und Kleinunternehmer in Österreich, mit den Sätzen für 2026 und Link zur jeweiligen amtlichen Quelle. Keine Anmeldung, keine Cookies, alles rechnet direkt im Browser.</p>
<ul class="cards">
<li><a href="{BASE}kleinunternehmergrenze/"><strong>Kleinunternehmergrenze 2026</strong><span>55.000 € brutto, Toleranz bis 60.500 € – bin ich noch Kleinunternehmer?</span></a></li>
<li><a href="{BASE}kilometergeld/"><strong>Kilometergeld 2026</strong><span>Pkw 0,50 €/km, Motorrad und Fahrrad 0,25 €/km, Mitfahrende 0,15 €/km</span></a></li>
<li><a href="{BASE}diaeten-inland/"><strong>Diäten Inland 2026</strong><span>Tagesgeld bis 30 €, 2,50 € je angefangene Stunde, Nächtigungsgeld 17 €</span></a></li>
</ul>
<h2>Hinweis zur Sozialversicherung (SVS)</h2>
<p>Hier gibt es bewusst keinen SVS-Rechner. Für Beiträge nutze bitte den offiziellen Rechner der <a href="https://www.svs.at/" rel="noopener">SVS</a>. Zur Orientierung einige Werte 2026 laut SVS:</p>
<ul>
<li>Versicherungsgrenze für Neue Selbständige: 6.613,20 € Einkünfte pro Jahr</li>
<li>Mindestbeitragsgrundlage Pensions- und Krankenversicherung: 551,10 € pro Monat</li>
<li>Höchstbeitragsgrundlage: 8.085,00 € pro Monat (97.020 € pro Jahr)</li>
<li>Unfallversicherung: 12,95 € pro Monat, unabhängig vom Einkommen</li>
</ul>
<p class="small">ESINT ist nicht die SVS und steht in keiner Verbindung zu ihr.</p>
{src("svs_neu","svs_beitr")}
{AD}''', "Rechner für Selbständige in Österreich 2026", js=False)

# --- Kleinunternehmer
page("kleinunternehmergrenze/", "Kleinunternehmergrenze Österreich 2026 Rechner – 55.000 € und Toleranz 60.500 € | ESINT",
 "Rechner zur Kleinunternehmerregelung in Österreich 2026: Umsatzgrenze 55.000 € brutto, 10-%-Toleranz bis 60.500 €. Prüfe, ob du noch ohne Umsatzsteuer verrechnen darfst.",
 f'''<p class="lead">Seit 1.1.2025 gilt in Österreich eine Umsatzgrenze von <strong>55.000 € brutto</strong> pro Jahr. Wird sie um nicht mehr als 10 % überschritten (also bis <strong>60.500 €</strong>), dürfen bis zum Jahresende weiter Rechnungen ohne Umsatzsteuer ausgestellt werden; im Folgejahr entfällt die Befreiung. Darüber sind alle weiteren Umsätze ab dem Überschreiten steuerpflichtig.</p>
<form class="calc" id="ku" onsubmit="return false">
<label>Umsatz im Vorjahr (brutto, €)<input type="number" inputmode="decimal" min="0" step="0.01" id="ku_vj" value="0"></label>
<label>Umsatz heuer bisher (brutto, €)<input type="number" inputmode="decimal" min="0" step="0.01" id="ku_bisher" value="0"></label>
<label>Geplanter neuer Umsatz / nächste Rechnung (brutto, €)<input type="number" inputmode="decimal" min="0" step="0.01" id="ku_neu" value="0"></label>
<output id="ku_out" aria-live="polite"></output>
</form>
<h2>So rechnet der Rechner</h2>
<ul>
<li>Vorjahr über 55.000 € → heuer keine Kleinunternehmerbefreiung (die Grenze darf weder im Vorjahr noch im laufenden Jahr überschritten sein).</li>
<li>Heuer gesamt bis 55.000 € → Befreiung bleibt.</li>
<li>Heuer gesamt über 55.000 € bis 60.500 € → Befreiung bis Jahresende, im Folgejahr nicht mehr.</li>
<li>Heuer gesamt über 60.500 € → ab dem Umsatz, mit dem die Grenze überschritten wird, ist Umsatzsteuer zu verrechnen.</li>
</ul>
<p>Nicht in die Grenze eingerechnet werden laut USP z. B. Hilfsgeschäfte (etwa Verkauf von Anlagegütern), bestimmte steuerfreie Umsätze und Reverse-Charge-Umsätze. Der Rechner berücksichtigt das nicht automatisch – gib nur die zählenden Umsätze ein. Sonderfälle (z. B. EU-Kleinunternehmerbefreiung, Option zur Steuerpflicht) deckt er nicht ab.</p>
{src("usp_ku","wko_ku")}
{AD}''', "Kleinunternehmergrenze 2026 – Rechner")

# --- Kilometergeld
page("kilometergeld/", "Kilometergeld Rechner Österreich 2026 – Pkw 0,50 €, Fahrrad 0,25 € | ESINT",
 "Kilometergeld Österreich 2026 berechnen: Pkw 0,50 €/km, Motorrad und Fahrrad 0,25 €/km, Zuschlag 0,15 €/km je Mitfahrer. Mit Jahresgrenzen und amtlichen Quellen.",
 f'''<p class="lead">Amtliches Kilometergeld seit 1.7.2025 (auch 2026 gültig): <strong>Pkw 0,50 €</strong>, <strong>Motorrad/Motorfahrrad 0,25 €</strong>, <strong>Fahrrad 0,25 €</strong> je Kilometer, dazu <strong>0,15 €</strong> je Kilometer für jede Mitfahrerin/jeden Mitfahrer.</p>
<form class="calc" id="km" onsubmit="return false">
<label>Fahrzeug<select id="km_typ"><option value="pkw">Pkw (0,50 €/km)</option><option value="moto">Motorrad / Motorfahrrad (0,25 €/km)</option><option value="rad">Fahrrad (0,25 €/km)</option></select></label>
<label>Gefahrene Kilometer<input type="number" inputmode="decimal" min="0" step="1" id="km_km" value="100"></label>
<label>Anzahl Mitfahrende (nur Pkw)<input type="number" inputmode="numeric" min="0" step="1" id="km_mit" value="0"></label>
<output id="km_out" aria-live="polite"></output>
</form>
<h2>Grenzen</h2>
<ul>
<li>Kraftfahrzeuge (Pkw, Motorrad): höchstens 30.000 km pro Kalenderjahr.</li>
<li>Fahrrad: höchstens 3.000 km pro Kalenderjahr (als Werbungskosten bei Arbeitnehmern).</li>
</ul>
<p>Mit dem Kilometergeld sind laut BMF u. a. Wertverlust, Treibstoff, Service, Versicherungen, Maut, Vignette und Parkgebühren abgegolten. Für Selbständige gelten eigene Regeln zur Nutzung des privaten Fahrzeugs im Betrieb – siehe USP.</p>
{src("km_bmf","km_oe","usp_reise")}
{AD}''', "Kilometergeld 2026 – Rechner")

# --- Diäten
page("diaeten-inland/", "Diäten Rechner Österreich 2026 – Tagesgeld 30 €, Nächtigungsgeld 17 € Inland | ESINT",
 "Tagesgeld und Nächtigungsgeld für Inlandsreisen in Österreich 2026 berechnen: bis 30 € pro Tag, 2,50 € je angefangene Stunde ab mehr als 3 Stunden, Nächtigung pauschal 17 €.",
 f'''<p class="lead">Inlandsreisen 2026: Tagesgeld bis <strong>30 €</strong> für 24 Stunden. Dauert die Reise länger als 3 Stunden, zählt jede angefangene Stunde ein Zwölftel, also <strong>2,50 €</strong>; ab mehr als 11 Stunden gibt es die vollen 30 €. Nächtigungsgeld pauschal <strong>17 €</strong> inkl. Frühstück, wenn keine höheren Kosten nachgewiesen werden.</p>
<form class="calc" id="di" onsubmit="return false">
<label>Reisedauer gesamt (Stunden)<input type="number" inputmode="decimal" min="0" step="0.25" id="di_h" value="8"></label>
<label>Nächtigungen (Pauschale 17 €)<input type="number" inputmode="numeric" min="0" step="1" id="di_n" value="0"></label>
<output id="di_out" aria-live="polite"></output>
</form>
<h2>So rechnet der Rechner</h2>
<ul>
<li>Bis einschließlich 3 Stunden: 0 €.</li>
<li>Über 3 Stunden: angefangene Stunden × 2,50 €, höchstens 30 € (volle 30 € ab mehr als 11 Stunden).</li>
<li>Längere Reisen: je volle 24 Stunden 30 €; den Rest rechnet der Rechner nach derselben Stundenregel. <em>Annahme von ESINT, nicht amtlich bestätigt:</em> Abrechnung nach 24-Stunden-Blöcken. § 26 Z 4 EStG erlaubt auch die Abrechnung nach Kalendertagen – dann kann das Ergebnis abweichen.</li>
</ul>
<p>Nicht berücksichtigt: Kürzungen bei bezahlten Mahlzeiten, Voraussetzungen der Reise (z. B. Entfernung, kein neuer Mittelpunkt der Tätigkeit) und Auslandsreisen. Für Selbständige gelten die Sätze laut USP als Betriebsausgaben, für Arbeitnehmer als steuerfreie Höchstbeträge.</p>
{src("ris26","usp_reise","usp_dienst")}
{AD}''', "Diäten Inland 2026 – Rechner")

# --- Impressum
page("impressum/", "Impressum, Haftung und Datenschutz | ESINT AT-Rechner",
 "Impressum, Haftungsausschluss und Datenschutzhinweis der ESINT AT-Rechner.",
 f'''<h2>Betreiber</h2>
<p>ESINT – GitHub-Konto <a href="https://github.com/esint-dev">esint-dev</a>. Kontakt: über <a href="https://github.com/esint-dev/at-rechner/issues">GitHub Issues</a>.</p>
<h2>Zweck</h2>
<p>Kostenlose Rechenhilfen zu Kleinunternehmergrenze, Kilometergeld und Diäten in Österreich. Die Seite enthält gekennzeichnete Werbung für eigene Produkte von ESINT (Excel-Vorlagen auf Gumroad).</p>
<h2>Haftungsausschluss</h2>
<p>Alle Ergebnisse sind unverbindlich und ohne Gewähr. Sie sind keine Steuer-, Rechts- oder Sozialversicherungsberatung. Gesetze und Sätze können sich ändern; maßgeblich sind die verlinkten amtlichen Quellen (BMF, USP, RIS, WKO, SVS). Stand der Werte: {STAND}. ESINT steht in keiner Verbindung zu BMF, SVS oder WKO.</p>
<h2>Datenschutz</h2>
<p>Die Rechner laufen vollständig im Browser. Eingaben werden nicht gespeichert oder übertragen. Es gibt keine Cookies, kein Tracking und keine Analyse-Skripte. Die Seite wird über GitHub Pages ausgeliefert; GitHub kann dabei technisch notwendige Server-Logs (z. B. IP-Adresse) verarbeiten – siehe <a href="https://docs.github.com/de/site-policy/privacy-policies/github-general-privacy-statement" rel="noopener">Datenschutzerklärung von GitHub</a>. Beim Klick auf einen Gumroad-Link gelten die Bestimmungen von Gumroad.</p>
<h2>Fehler gefunden?</h2>
<p>Bitte über <a href="https://github.com/esint-dev/at-rechner/issues">GitHub Issues</a> melden – mit Link zur amtlichen Quelle.</p>''', "Impressum, Haftung, Datenschutz", js=False)

# --- 404, robots, sitemap, key, .nojekyll
(OUT/"404.html").write_text(f'<!doctype html><html lang="de-AT"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Seite nicht gefunden | ESINT AT-Rechner</title><meta name="robots" content="noindex"><link rel="stylesheet" href="{BASE}style.css"></head><body><main><h1>Seite nicht gefunden</h1><p><a href="{BASE}">Zur Übersicht der Rechner</a></p></main></body></html>\n', encoding="utf-8")
(OUT/"robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {BASE}sitemap.xml\n")
urls = [p for p,_ in NAV]
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"  <url><loc>{BASE}{p}</loc><lastmod>2026-11-11</lastmod></url>\n" for p in urls) + "</urlset>\n"
(OUT/"sitemap.xml").write_text(sm)
(OUT/f"{KEY}.txt").write_text(KEY)
(OUT/".nojekyll").write_text("")
for f in ["style.css","app.js"]:
    (OUT/f).write_text(open(f, encoding="utf-8").read(), encoding="utf-8")
(OUT/"README.md").write_text(f"# ESINT AT-Rechner\n\nKostenlose Rechner für Selbständige in Österreich 2026: Kleinunternehmergrenze, Kilometergeld, Diäten Inland.\n\nLive: {BASE}\n\nAlle Sätze mit amtlicher Quelle und Abrufdatum auf der jeweiligen Seite. Unverbindlich, keine Steuerberatung.\n\nAnzeige (eigenes Produkt): Kleinunternehmer-Excel – https://gumroad.com/l/hipixo (gratis Lite)\n", encoding="utf-8")
print("ok", sorted(str(p) for p in OUT.rglob("*") if p.is_file()))
