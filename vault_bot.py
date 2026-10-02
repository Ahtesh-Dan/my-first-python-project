import sqlite3
conn = sqlite3.connect("company_vault.db" )
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY,
        name TEXT,
        department TEXT
    )
''')
conn.commit()
conn.close()
print("✅ Vault Created and 'employees' table is ready!")