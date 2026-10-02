import sqlite3
conn =  sqlite3.connect("admission_vault.db")
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        branch TEXT
    )
''')
conn.commit()
print("🎓 Welcome to AKS University Admission Portal 🎓")
print("------------------------------------------------")
print("(Software band karne ke liye Name mein 'exit' type karein)\n")
while True:
    student_name = input("Enter the studen Name : " )
    if student_name.lower() == 'exit' :
        break
    student_branch= input("Enter branch(e.g., 'CIVIL','Mechanical','Electrical'):")
    cursor.execute("INSERT INTO students(name,branch) VALUES (?,?)",(student_name,student_branch))
    conn.commit()
    print(f'Admission confirmed:{student_name} {student_branch} ka data vaukt me lock ho gya hai ! \n')
conn.close()
print("🚪 Software Closed. Saara admission data perfectly safe hai.")
                                                
