import os
folder_address = os.path.dirname(os.path.abspath(__file__))
target_folder = os.path.join(folder_address,"company_server")
print(f"Radar on : scanning start{target_folder}")
print("_" * 40)
scanned_items = os.listdir(target_folder)
for item in scanned_items:
    print(f"found {item}")
print("-" * 40)
print("✅ Scan Complete, Chief!")