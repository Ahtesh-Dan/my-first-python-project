import sqlite3
conn =  sqlite3.connect("company_vault.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM  Employees WHERE department = 'IT'" )
it_records = cursor.fetchall()
print("smart Radar Result(Only IT departments):")
print("---" * 40)
for records in it_records:
    print(records)
print("-----" * 40)
conn.close()