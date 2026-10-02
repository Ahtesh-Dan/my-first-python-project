import csv
import os
import json
folder_address = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(folder_address,"live_jokes_data.csv")
json_file = os.path.join(folder_address,"cloud_jokes_data.json")
print("Data migration pipe line start ho rhe hai--------------")
print("🔍 Bot is opening the Excel file...\n")
print("-" * 50)
cloud_data = []
try:
    with open(csv_file,mode="r",encoding="utf-8") as file:
        reader = csv.reader(file)
        next (reader)
        for row in reader:
            if len(row) >= 3:
                joke_dict = {"id":row[0],"question":row[1],"answer":row[2]}
                cloud_data.append(joke_dict)
    print("✅ Step 1: CSV data successfully Dictionary list mein badal gaya!")
    with open(json_file, mode="w", encoding="utf-8") as j_file:
        json.dump(cloud_data, j_file, indent=4)

    print("🚀 Step 2: Success! Data successfully 'cloud_jokes_data.json' mein migrate ho gaya!")
except Exception as e:
    print(f"⚠️ ERROR: Lagta hai file nahi mili. Detail: {e}")
print("-" * 50)
print("\n✅ Reading Complete! Bot ne aapki Excel file successfully padh li!")