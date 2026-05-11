Questo programma è scritto in Python e permette di gestire le proprie spese utilizzando un database SQLite.

Con questo software è possibile:

-Inserire categorie di spesa
-Registrare spese
-Impostare budget mensili
-Visualizzare le spese effettuate e confrontarle con i budget inseriti

REQUISITI:

Per eseguire il programma è necessario:

-Python 3.x
-Nessuna libreria esterna da installare


É stata utilizzata la libreria sqlite3 (già inclusa in Python)


ISTRUZIONI PER L’ESECUZIONE

1. Assicurati di avere Python installato

2. Assicurati che i file main.py e database.sql siano nella stessa cartella

3. Esegui main.py con un doppio click oppure aprendo il terminale nella cartella ed eseguendo il comando python main.py


All'avvio verrá creato il database database.db (se non esiste) ed eseguito lo script database.sql

Successivamente,il programma mostra questo menu:

1 - Inserisci Categoria
2 - Inserisci Spesa
3 - Inserisci Budget Mensile
4 - Visualizza Report
5 - Esci

1) Inserisci Categoria

-Permette di aggiungere una nuova categoria
-Non permette duplicati

2) Inserisci Spesa

-Data (da inserire in formato YYYY-MM-DD es. 2026-05-11)
-Importo (deve essere positivo,importi decimali vanno inseriti nel formato "ab.cd")
-Categoria della spesa (da inserire tra quelle disponibili)
-Descrizione / Note sulla spesa

3) Inserisci Budget

-Imposta un budget mensile per categoria (formato YYYY-MM come sopra)
-Se esiste già un budget per quel mese esso viene aggiornato

4) Visualizza report

-Totale spese per categoria (mostra la somma delle spese divise per categoria)

-Spese vs Budget (confronta le spese con i budget impostati)

-Elenco spese (mostra tutte le spese ordinate per data)


