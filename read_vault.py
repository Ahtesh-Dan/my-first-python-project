import sqlite3
conn = sqlite3.connect("company_vault.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM employees")
all_records = cursor.fetchall()
print("📋 Vault ka Data (Live from Database):")
print("-" * 40)
for record in all_records:
    print(record)
