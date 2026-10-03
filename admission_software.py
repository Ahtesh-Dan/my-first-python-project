import sqlite3
from  google import genai
client=genai.Client(api_key="MERA PASSWORD")
conn = sqlite3.connect("aks_Univerity.db")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS admission_leads 
 (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, interest TEXT, ai_suggested_branch TEXT)''')hhd    
print("🎓 AKS University - Smart Admission Cell mein aapka swagat hai!\n")
student_name = input("student ka naam darj karein")
student_interest= input(f'{student_name} ko kis cheez me interest hai ? (jaise- computer, machine,kheti ):')
prompt = f"ek student jis ka naam {student_name} hai ,usey {student_interest} main interest hai KS University Satna ke hisaab se use sirf 1 line mein ek best engineering ya degree branch suggest karo."
response=client.models.generate_content(model="gemini-3.8-flash",contents=prompt )
ai_suggestion=response.text.strip()
print("--"  * 40)
print(f"Ai ki salah:{ai_suggestion}")
print("--" * 50)
cursor.execute("INSERT INTO admission_leads (name, interest, ai_suggested_branch) VALUES (?, ?, ?)", (student_name, student_interest, ai_suggestion))
conn.commit()
print("\n✅ Success: Student ka data aur AI ki salah tijori (Database) mein safely lock ho gayi!")
conn.close()