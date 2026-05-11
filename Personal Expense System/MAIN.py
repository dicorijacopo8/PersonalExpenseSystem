import sqlite3

conn = sqlite3.connect("database.db")
conn.execute("PRAGMA foreign_keys = ON")

print("START")

f = open("database.sql", "r", encoding="utf-8")
sql = f.read()
f.close()

conn.executescript(sql)

print("DATABASE CARICATO")

# _____________________
# MENU PRINCIPALE
# _____________________

def menu_principale():
    while True:
        print("""

SISTEMA SPESE PERSONALI

1 - Inserisci Categoria
2 - Inserisci Spesa
3 - Inserisci Budget Mensile
4 - Visualizza Report
5 - Esci

""")

        scelta = input("Scelta: ")

        if scelta == "1":
            inserisci_categoria()
        else:
            if scelta == "2":
                inserisci_spesa()
            else:
                if scelta == "3":
                    inserisci_budget()
                else:
                    if scelta == "4":
                        menu_report()
                    else:
                        if scelta == "5":
                            print("Uscita")
                            break
                        else:
                            print("Scelta non valida")


# _____________________
# CATEGORIE
# _____________________

def inserisci_categoria():
    nome = input("Nome categoria: ")
    if nome == "":
        print("Inserisci un nome valido")
        return

    for row in conn.execute("SELECT nome FROM categorie"):
        if row[0] == nome:
            print("Categoria già esistente")
            return

    conn.execute("INSERT INTO categorie (nome) VALUES (?)", (nome,))
    conn.commit()
    print("Categoria inserita")


# _____________________
# SPESA
# _____________________

def inserisci_spesa():
    print("\nCategorie disponibili:")
    for row in conn.execute("SELECT nome FROM categorie"):
        print("-", row[0])

    data = input("Data (YYYY-MM-DD): ")

    if len(data) != 10:
        print("Errore data")
        return
    else:
        if data[4] != "-" or data[7] != "-":
            print("Errore data")
            return

    importo = float(input("Importo: "))

    if importo <= 0:
        print("Errore importo")
        return

    categoria = input("Categoria: ")
    descrizione = input("Descrizione: ")

    categoria_id = None

    for row in conn.execute("SELECT id FROM categorie WHERE nome = ?", (categoria,)):
        categoria_id = row[0]

    if categoria_id is None:
        print("Categoria non trovata")
        return

    conn.execute(
        "INSERT INTO spese (data, importo, categoria_id, descrizione) VALUES (?, ?, ?, ?)",
        (data, importo, categoria_id, descrizione)
    )

    conn.commit()
    print("Spesa inserita")


# _____________________
# BUDGET
# _____________________

def inserisci_budget():
    print("\nCategorie disponibili:")
    for row in conn.execute("SELECT nome FROM categorie"):
        print("-", row[0])

    mese = input("Mese (YYYY-MM): ")

    if len(mese) != 7:
        print("Errore mese")
        return
    else:
        if mese[4] != "-":
            print("Errore mese")
            return

    importo = float(input("Budget: "))
    categoria = input("Categoria: ")

    if importo <= 0:
        print("Errore budget")
        return

    categoria_id = None

    for row in conn.execute("SELECT id FROM categorie WHERE nome = ?", (categoria,)):
        categoria_id = row[0]

    if categoria_id is None:
        print("Categoria non trovata")
        return

    esiste = False

    for row in conn.execute(
        "SELECT id FROM budget WHERE mese = ? AND categoria_id = ?",
        (mese, categoria_id)
    ):
        esiste = True

    if esiste:
        conn.execute(
            "UPDATE budget SET importo = ? WHERE mese = ? AND categoria_id = ?",
            (importo, mese, categoria_id)
        )
        print("Budget aggiornato")
    else:
        conn.execute(
            "INSERT INTO budget (mese, categoria_id, importo) VALUES (?, ?, ?)",
            (mese, categoria_id, importo)
        )
        print("Budget inserito")

    conn.commit()


# _____________________
# REPORT
# _____________________

def menu_report():
    while True:
        print("""
1- Totale spese per categoria
2- Elenco spese
3- Spese vs budget
4- Ritorna
""")

        scelta = input("Scelta: ")

        if scelta == "1":
            report_totale_categoria()
        else:
            if scelta == "2":
                report_spese()
            else:
                if scelta == "3":
                    report_budget()
                else:
                    if scelta == "4":
                        break
                    else:
                        print("Scelta non valida")


def report_totale_categoria():
    for row in conn.execute("""
        SELECT c.nome, SUM(s.importo) || '€'
        FROM spese s, categorie c
        WHERE s.categoria_id = c.id
        GROUP BY c.nome
    """):
        print(row)


def report_budget():
    query = """
        SELECT 
            b.mese,
            c.nome,
            b.importo,
            SUM(s.importo) AS speso
        FROM budget b
        JOIN categorie c 
            ON b.categoria_id = c.id
        JOIN spese s 
            ON s.categoria_id = b.categoria_id
            AND s.data LIKE b.mese || '%'
        GROUP BY b.mese, c.nome, b.importo
        ORDER BY b.mese, c.nome
    """
    for mese, nome_categoria, budget, speso in conn.execute(query):
        if speso > budget:
            stato = "SUPERAMENTO BUDGET"
        else:
            stato = "OK"
        print("Mese:", mese)
        print("Categoria:", nome_categoria)
        print("Il budget é", budget, "€")
        print("Hai speso", speso, "€")
        print(stato)
        print()

def report_spese():
    query = """
        SELECT 
            spese.data,
            categorie.nome,
            spese.importo,
            spese.descrizione
        FROM spese
        JOIN categorie 
            ON spese.categoria_id = categorie.id
        ORDER BY spese.data
    """
    print("Le tue spese:")
    print("____________________________________________________________________")
    for data, nome_categoria, importo, descrizione in conn.execute(query):
        print(data, "-", nome_categoria,"-", importo, "€","-", descrizione)

# _____________________

menu_principale()
conn.close()