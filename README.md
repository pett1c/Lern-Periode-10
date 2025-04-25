# Lern-Periode 10

25.4 bis 27.6

## Grob-Planung

1. Welche Programmiersprache möchten Sie verwenden? Was denken Sie, wo Ihre Zeit und Übung am sinnvollsten ist?
Ich möchte Python verwenden, da ich mich nach den ersten Schritten mit Modul 259 und der Godot-Spielengine sehr für Python interessiere.

2. Welche Datenbank-Technologie möchten Sie üben? Fühlen Sie sich sicher mit SQL und möchten etwas Neues ausprobieren; oder möchten Sie sich weiter mit SQL beschäftigen?
Ich möchte gerne versuchen, mit MongoDB zu arbeiten.

3. Was wäre ein geeignetes Abschluss-Projekt?
Ich implementiere einen „Musikempfehlungsdienst“. Er funktioniert ähnlich wie das Beispiel aus LP10.pptx (Empfehlungs-System für Koch-Rezepte), aber ein bisschen anders: Der Benutzer beantwortet Fragen zu Stimmung, Tempo und anderen Merkmalen, und das System schlägt einen Song/Genre/Künstler aus der Datenbank vor. Anhand der Kriterien bewertet der Nutzer die Empfehlung am Ende und das System lernt aus dem Feedback. 

## 25.4

Welche 3 *features* sind die wichtigsten Ihres Projektes? Wie können Sie die Machbarkeit dieser in jeweils 45' am einfachsten beweisen?

- [x] *make or break feature* 1: Einfache Musikdatenbank mit kategorisierten Songs (nach Stimmung, Tempo, Genre, usw...)
- [x] *make or break feature* 2: Grundlegender Empfehlungsalgorithmus basierend auf Benutzerantworten
- [x] *make or break feature* 3: Minimale Benutzerinterface für Eingabe und Anzeige von Empfehlungen


Heute habe ich einen einfachen Prototyp mit drei grundlegenden Funktionen erstellt. Zuerst habe ich eine Datenbank implementiert, in der ich eine Tabelle mit Liedern hinzugefügt habe, und dann habe ich einen Test zum Füllen der Tabelle implementiert. Wenn die Tabelle nicht gefüllt ist, fülle ich sie mit Testdaten von fünf Liedern (später werde ich eine große Anzahl verschiedener Lieder für die Datenbank sammeln), die unterschiedliche Stimmungen, Tempi und Genres haben.
Als Nächstes habe ich einen Test implementiert, um diese Funktion zu validieren, und anschließend eine Klasse zum Abrufen der Empfehlung erstellt. In dieser Klasse gibt das System die verfügbaren Stimmungen und Tempi zurück. Ich habe auch einen Test implementiert, um diese Funktion zu überprüfen, und bin dann zum letzten Punkt übergegangen: der Implementierung einer einfachen Benutzeroberfläche direkt in der Konsole (später werde ich eine normale und schön aussehende Oberfläche implementieren). Ich habe auch die Hauptdatei (main.py) implementiert und das ist das Ende der Arbeit für heute.

☝️ Vergessen Sie nicht, den Code von heute auf github hochzuladen. Ggf. bietet es sich an, für die Code-Schnipsel einen eigenen Ordner `exploration` zu erstellen.

## 2.5

Ausgehend von Ihren Erfahrungen vom 25.4, welche *features* brauchen noch mehr Recherche? (Sie können auch mehrere AP für ein *feature* aufwenden.)

- [ ] Einen Layout für kommende GUI erstellen (📵)
- [ ] Erweiterung des Datenbankenschemas: Hinzufügen von zusätzlichen Attributen für Songs (z. B. Popularität, Sprache, usw...)
- [ ] Implementierung einer Feedback-Funktion

✍️ Heute habe ich... (50-100 Wörter)

☝️ Vergessen Sie nicht, den Code von heute auf github hochzuladen.

## 9.5

Planen Sie nun Ihr Projekt, sodass die *Kern-Funktionalität* in 3 Sitzungen realisiert ist. Schreiben Sie dazu zunächst 3 solche übergeordneten Kern-Funktionalitäten auf: 

1. Kern-Funktionalität
2. Kern-Funktionalität
3. Kern-Funktionalität

Diese Kern-Funktionalitäten brechen Sie nun in etwa 4 AP je herunter. Versuchen Sie jetzt bereits, auch die Sitzung vom 16.5 und 23.5 zu planen (im Wissen, dass Sie kleine Anpassungen an Ihrer Planung vornehmen können).

- [ ] ...
- [ ] ...
- [ ] ...

✍️ Heute habe ich... (50-100 Wörter)

☝️  Vergessen Sie nicht, den Code von heute auf github hochzuladen.

## 16.5

- [ ] ...
- [ ] ...
- [ ] ...
- [ ] ...

✍️ Heute habe ich... (50-100 Wörter)

☝️  Vergessen Sie nicht, den Code von heute auf github hochzuladen.

## 23.5

- [ ] ...
- [ ] ...
- [ ] ...
- [ ] ...

✍️ Heute habe ich... (50-100 Wörter)

☝️  Vergessen Sie nicht, den Code von heute auf github hochzuladen.

## 6.6

Ihr Projekt sollte nun alle Funktionalität haben, dass man es benutzen kann. Allerdings gibt es sicher noch Teile, welche "schöner" werden können: Layout, Code, Architektur... beschreiben Sie kurz den Stand Ihres Projekts, und leiten Sie daraus 6 solche "kosmetischen" AP für den 6.6 und den 13.6 ab.

- [ ] ...
- [ ] ...
- [ ] ...
- [ ] ...

✍️ Heute habe ich... (50-100 Wörter)

☝️  Vergessen Sie nicht, den Code von heute auf github hochzuladen.

## 13.6

- [ ] ...
- [ ] ...

✍️ Heute habe ich... (50-100 Wörter)

☝️  Vergessen Sie nicht, den Code von heute auf github hochzuladen.

## 20.6

Was fehlt Ihrem fertigen Projekt noch, um es auszuliefern? Reicht die Zeit für ein *nice-to-have feature*?

- [ ] ...

Bereiten Sie in den verbleibenden 2 AP Ihre Präsentation vor

- [ ] Materialien der Präsentation vorbereiten
- [ ] Präsentation üben

✍️ Heute habe ich... (50-100 Wörter)

☝️  Vergessen Sie nicht, die Unterlagen für Ihre Präsentation auf github hochzuladen.

## 27.6
