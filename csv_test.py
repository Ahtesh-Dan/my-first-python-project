import csv
import os
folder_address = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(folder_address,"dreams_target.csv")
with open(csv_file, mode="w",newline="",encoding="utf-8") as file:
    writer=csv.writer(file)
    writer.writerow(["ID","Name","Future role","Target company"])
    writer.writerow([1,"chief","Senior Cloude Devs Ops","Amazon AWS"])
    writer.writerow([2, "Professor", "AI Mentor", "Google"])
print("🔥 CSV Ready! Left panel mein 'dream_target.csv' check kijiye!")