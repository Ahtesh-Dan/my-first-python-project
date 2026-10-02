import sqlite3
conn = sqlite3.connect("company_vault.db")
cursor =conn.cursor()
cursor.execute("INSERT INTO EMPLOYEES(name,department) VALUES ('RAHUL','IT')")
cursor.execute("INSERT INTO EMPLOYEES(name,department) VALUES('Amit','HR')")
cursor.execute("INSERT INTO EMPLOYEES(name,department) VALUES ('Neha','Finance')")
conn.commit()
conn.close()
print("✅ Data successfully saved in Vault!")

