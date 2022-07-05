# Password Manager mit Python

## Abhängigkeiten
python3:
- re
- os
- sys
- platform
- zipfile
- pyperclip
- PyQt5
- configparser
- cryptography

## Todo
### window.py aufteilen

Die Datenbankfunktionen aus window.py sollen nach database.py ausgelagert werden:
- new_base
- open_base
- close_base

### Kryptographie verbessern
Das Passwort nicht mit random-seed verschlüsseln, sondern als seed für den Hash-Schlüssel nutzen

(Verhinderung von Reverse-Engineering)

### Auto-Updater
Script, dass Repo bei Bedarf von Github klont (Dafür Datenbanken in anderes Verzeichnis verschieben)

### Features zur UI hinzufügen (nach der Aufteilung)
- Zusätzliches Feld für E-Mail Adresse
- Zusätzliches Feld für Notizen

### Bau als ausführbare Datei
- Export für Windows
- Export für Linux
- statisch gelinkt