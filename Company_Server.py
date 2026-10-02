import os
folder_name=os.path.dirname(os.path.abspath(__file__))
real_folder = os.path.join(folder_name,"company_server")
departments = ["HR", "IT", "Finance"]
for dept in departments:
    final_path = os.path.join(real_folder, dept)
    os.makedirs(final_path,exist_ok=True)
    print(f"ready {dept}")
    print("-" * 50)
print("🏁 Mission Complete: Andar jaakar check kijiye")