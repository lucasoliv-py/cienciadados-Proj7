import sqlite3 as sql
from sqlite 3 import Cursor

# Requisito RS2 - Inserção de dados
def inserir(registro: list) -> sql.Cursor:
    
    """ Esta função permite ao usuário inserir dados no banco Agenda.db """
    
    conn = sql.connect("Agenda.db")
    conn.cursos()
    conn.execute("""
    INSERT INTO Contatos values registro;""")
    
### Requisito RS3 - Consulta de dados


### Requisito RS4 - Atualização de dados


### Requisito RS5 - Exclusão de dados