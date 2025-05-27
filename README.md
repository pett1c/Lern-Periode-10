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

- [x] Einen Layout für kommende GUI erstellen (📵)
- [x] Erweiterung des Datenbankenschemas: Hinzufügen von zusätzlichen Attributen für Songs (z. B. Popularität, Sprache, usw...)
- [x] Implementierung einer Feedback-Funktion

Als erstes habe ich heute die Datenbank erweitert, indem ich einige zusätzliche Lieder hinzugefügt habe (mit Hilfe von KI) und die Anzahl der Attribute erweitert habe, indem ich das Entstehungsjahr des Liedes, den Gesangs-/Instrumental-Typ, wenn der Gesangs-Typ dann in welcher Sprache, und auch eine Beliebtheitsskala hinzugefügt habe. Die nächste Aufgabe war die Implementierung der Bewertungs- und Feedbackfunktion im Allgemeinen - ich implementierte das Speichern der Bewertung und bearbeitete auch das Empfehlungssystem, so dass die Lieder mit der höchsten Bewertung mit größerer Wahrscheinlichkeit weitergegeben wurden. Das letzte, was ich implementiert habe, war ein Layout der Benutzeroberfläche auf Papier, aber ich denke immer noch über ein vollwertiges Layout nach. Im Moment habe ich nur eine grundlegende GUI implementiert, ohne mich auf meine eigene Arbeit zu konzentrieren.

☝️ Vergessen Sie nicht, den Code von heute auf github hochzuladen.

## 9.5

Planen Sie nun Ihr Projekt, sodass die *Kern-Funktionalität* in 3 Sitzungen realisiert ist. Schreiben Sie dazu zunächst 3 solche übergeordneten Kern-Funktionalitäten auf: 

1. Erweiterte Datenbankstruktur und Datensammlung
2. Verbesserter Empfehlungsalgorithmus mit Machine Learning
3. Komplette GUI mit erweiteren Funktionen

Diese Kern-Funktionalitäten brechen Sie nun in etwa 4 AP je herunter. Versuchen Sie jetzt bereits, auch die Sitzung vom 16.5 und 23.5 zu planen (im Wissen, dass Sie kleine Anpassungen an Ihrer Planung vornehmen können).

### 1. Erweiterte Datenbankstruktur und Datensammlung (für heute):
- [x] ~~Umfangreiches Datenbankschema erstellen (mit detaillierten Attributen wie BPM, Subgenres, usw.)~~
- [x] ~~Recherche und Sammlung von Daten zu experimenteller elektronischer Musik~~

### 2. Verbesserter Empfehlungsalgorithmus mit Machine Learning (16.5):
- [x] ~~Grundlegende Datenanalyse führen und Muster identifizieren~~
- [x] ~~Einfaches Machine Learning-Modell implementieren~~
- [x] ~~Modell mit vorhandenen Popularität-Daten trainieren~~
- [x] ~~Optimierung des Modells~~

### 3. Komplette GUI mit erweiterten Funktionen (23.5):
- [x] ~~Detaillierte Benutzeroberfläche mit CustomTkinter entwerfen~~
- [x] ~~Erstellen Sie die Auswirkungen von Nutzerbewertungen auf die Popularität von Titeln (Feedback)~~
- [ ] ~~SoundCloud API implementieren, um einen bestimmten Track schön anzuzeigen (manchmal sind Tracknamen völlig unverständlich)~~

Heute habe ich versucht, mir einen schönen Datensatz mit experimenteller Musik zu erstellen. Zu Beginn habe ich neue Attribute abgeleitet, nach denen ich Tracks sammeln werde. Später, je mehr ich mir logische und notwendige Attribute überlegte, desto schwieriger wurde es, einen Datensatz mit genügend Informationen zu realisieren. Bei dem Versuch, wenigstens einige Titel zu sammeln, wurde mir schliesslich klar, dass dies nicht funktionieren würde, und ich beschloss, einen fertigen Datensatz mit Titeln zu finden, die bereits experimentell sind oder die ich durch Entfernen aller nicht experimentellen Titel „bearbeiten“ würde. Bei der Analyse der verfügbaren Datensätze wurde mir klar, dass entweder die von mir benötigten Attribute nicht vorhanden sind, der Datensatz aber gross genug ist, um ihn zu bearbeiten, oder dass die Attribute vorhanden sind, der Datensatz aber zu klein ist bzw. keine experimentellen Genres enthält. So entschied ich schliesslich, dass die Idee, experimentelle Titel für den Datensatz zu sammeln und auf dieser Grundlage das Modell für weitere Empfehlungen zu trainieren, auf dem Papier sicherlich gut ist, aber in der Umsetzung des Problems: das Finden/Erstellen des Datensatzes selbst zum Trainieren des Modells. Ich könnte es tun, aber leider habe ich nicht viel Zeit, um das Projekt selbst zu realisieren. Also werde ich einfach einen Datensatz mit den benötigten Attributen nehmen und mit einem normalen Datensatz arbeiten.

☝️  Vergessen Sie nicht, den Code von heute auf github hochzuladen.

## 16.5

### 2. Verbesserter Empfehlungsalgorithmus mit Machine Learning:
- [x] Grundlegende Datenanalyse führen und Muster identifizieren
- [x] Einfaches Machine Learning-Modell implementieren
- [x] Modell mit vorhandenen Feedback-Daten trainieren
- [x] Optimierung des Modells

Als erstes habe ich heute einen [Datensatz](https://www.kaggle.com/datasets/devdope/200k-spotify-songs-light-dataset/) gefunden, der meinen Bedürfnissen entspricht, und ihn dann analysiert. Die Analyse (`csv_analysis.py`) hat gezeigt, dass es eine Menge „Müll“ in der Datenbank gibt, der entfernt werden sollte. Also habe ich `clean_db.py` geschrieben, das die notwendigen Felder von „Müll“ bereinigt (z.B. gab es bei den Genres eine riesige Menge an einfach nur seltsamen Genres oder Genres in Form von Tags (`'pop rock, rock, ...'`)). Eine zweite Analyse (`db_analysis.py`) zeigte, dass die Datenbank nun für das Modelltraining bereit war. Der nächste und letzte Schritt bestand darin, ein Modell (`recommendation.py`) zu entwickeln, das Lieder auf der Grundlage der ausgewählten Stimmung vorhersagen kann. Später werde ich dieses Modell an die von mir benötigte GUI anpassen.

☝️  Vergessen Sie nicht, den Code von heute auf github hochzuladen.

## 23.5

- [x] Detaillierte Benutzeroberfläche mit CustomTkinter entwerfen
- [x] Erstellen Sie die Auswirkungen von Nutzerbewertungen auf die Popularität von Titeln (Feedback)
- [x] Hinzufügen der Möglichkeit, den Titel zu kopieren

Heute war ein schwieriger, aber produktiver Tag. Als erstes habe ich ein Mockup auf der Grundlage meiner Zeichnung (siehe `2.5`) erstellt, um die Schnittstelle mit `CustomTkinter` grob nachzubilden. Als nächstes habe ich mir Gedanken über eine angemessene Feedback-Funktion gemacht, und für mich war die beste Option, den bereits vorhandenen Popularitätswert jedes Tracks mit Sternen zu beeinflussen. So nimmt 1 Stern 2 vom Beliebtheitswert weg, 2 Sterne nehmen 1 vom Beliebtheitswert weg, 3 Sterne nehmen nicht weg, fügen aber auch nicht hinzu, 4 Sterne fügen 1 zum Beliebtheitswert hinzu, 5 Sterne fügen 2 zum Beliebtheitswert hinzu. Ausserdem dachte ich darüber nach, die Funktion des Kopierens von Titeln bei Klick zu implementieren (unter Verwendung der `pyperclip`-Bibliothek), da dies sehr praktisch wäre. Danach habe ich begonnen, alle oben genannten Punkte zu implementieren. Letztendlich konnte ich das meiste davon erfolgreich umsetzen, aber am Ende war das Programm extrem langsam und unoptimiert, was nicht in erster Linie an der fehlenden Architektur lag. Ich werde das Programm optimieren, eine richtige Architektur erstellen, einige kleinere Fehler beheben und all das in `6.6`.

☝️  Vergessen Sie nicht, den Code von heute auf github hochzuladen.

## 6.6

Ihr Projekt sollte nun alle Funktionalität haben, dass man es benutzen kann. Allerdings gibt es sicher noch Teile, welche "schöner" werden können: Layout, Code, Architektur... beschreiben Sie kurz den Stand Ihres Projekts, und leiten Sie daraus 6 solche "kosmetischen" AP für den 6.6 und den 13.6 ab.

- [ ] Optimierung
- [ ] Schaffung einer angemessenen Architektur
- [ ] Fehlerkorrekturen
- [ ] Verbesserungen der Benutzeroberfläche

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
