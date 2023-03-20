import sqlite3

conn = sqlite3.connect('test.db')
print ("Opened database successfully")
#[{"coordsBloc" : [], "idBloc" : 0, "typeBloc" : 0, "color" : ""}]
conn.execute('''CREATE TABLE LISTE_BLOC
            (ID INT PRIMARY KEY     NOT NULL,
            IDBLOC          INT     NOT NULL,
            TYPEBLOC        INT     NOT NULL,
            COLOR           TEXT    NOT NULL)
            ''')
conn.commit()

conn.close()