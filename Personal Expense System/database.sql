-- TABELLE


CREATE TABLE IF NOT EXISTS categorie (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS spese (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data TEXT NOT NULL,
    importo REAL NOT NULL CHECK (importo > 0),
    categoria_id INTEGER NOT NULL,
    descrizione TEXT,
    UNIQUE (data, importo, categoria_id, descrizione),
    FOREIGN KEY (categoria_id) REFERENCES categorie(id)
);

CREATE TABLE IF NOT EXISTS budget (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    mese TEXT NOT NULL,
    categoria_id INTEGER NOT NULL,
    importo REAL NOT NULL CHECK (importo > 0),
    UNIQUE (mese, categoria_id),
    FOREIGN KEY (categoria_id) REFERENCES categorie(id)
);

-- Inserimenti:

-- CATEGORIE

INSERT or IGNORE INTO categorie (nome) VALUES
('Alimentari'),
('Automobile'),
('Svago'),
('Libri&Manga');

-- SPESE

INSERT or IGNORE INTO spese (data, importo, categoria_id, descrizione) VALUES
('2026-05-01', 20, 1, 'Frutta e verdura'),
('2026-05-04', 20, 2, 'Diesel'),
('2026-05-04', 20, 2, 'Autostrada'),
('2026-05-07', 13, 3, 'Netflix'),
('2026-04-30', 5, 4, 'One Piece vol.100');

-- BUDGET

INSERT or IGNORE INTO budget (mese, categoria_id, importo) VALUES
('2026-05', 1, 300),
('2026-05', 3, 100),
('2026-05', 2, 200);
